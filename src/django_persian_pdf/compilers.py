import logging
import os
from abc import ABC, abstractmethod
from subprocess import PIPE, CalledProcessError, run
from tempfile import NamedTemporaryFile, mkdtemp, mkstemp

logger = logging.getLogger(__name__)


class BaseCompiler(ABC):
    build_engine: str = None
    template_file_suffix: str = None

    def __init__(self, template_string: str):
        self.template_string = template_string
        self.temporary_build_folder = None
        self.temporary_build_file = None
        self.pdf_file = NamedTemporaryFile(suffix='.pdf')
        self.pdf_file.close()

    def clean_string(self) -> str:
        return self.template_string

    @abstractmethod
    def get_compile_command(self) -> str:
        pass

    def build(self):
        clean_string = self.clean_string()
        self.temporary_build_folder = mkdtemp()
        temp_file, self.temporary_build_file = mkstemp(
            suffix=self.template_file_suffix, dir=self.temporary_build_folder
        )
        os.write(temp_file, str.encode(clean_string))
        os.close(temp_file)

    def compile(self):
        self.build()

        cmd = self.get_compile_command()
        try:
            run(cmd, shell=True, stdout=PIPE, stderr=PIPE, check=True)  # noqa

        except CalledProcessError as called_process_error:
            logger.error(f'Failed compiling the pdf with error: {called_process_error.output}')

        return self.read()

    def read(self):
        pdf_contents = ''
        try:
            with open(self.pdf_file.name, 'rb') as f:
                pdf_contents = f.read()

        except FileNotFoundError as err:
            logger.error('Failed reading pdf file %s', err)
        return pdf_contents


class LatexCompiler(BaseCompiler):
    build_engine = 'xelatex'

    def clean_string(self):
        clean_string = self.template_string.replace('ـ', '-')
        clean_string = clean_string.replace('"', '\\"')
        clean_string = clean_string.replace("'", "\\'")
        clean_string = clean_string.replace('ي', 'ی')
        return clean_string

    def get_compile_command(self) -> str:
        cmd = f'{self.build_engine} -halt-on-error -output-directory={self.temporary_build_folder} {self.temporary_build_file}'
        return cmd

    def read(self):
        pdf_contents = ''
        try:
            f = open(self.temporary_build_file + '.pdf', 'rb')  # noqa
            pdf_contents = f.read()
            f.close()
        except FileNotFoundError as err:
            logger.error(f'Failed reading pdf file: {err}')
        return pdf_contents


class ChromeCompiler(BaseCompiler):
    build_engine = 'google-chrome-stable'
    template_file_suffix = '.html'

    def get_compile_command(self) -> str:
        cmd = f'{self.build_engine} --headless --no-sandbox --disable-gpu --print-to-pdf-no-header --print-to-pdf-no-footer --print-to-pdf={self.pdf_file.name} {self.temporary_build_file}'
        return cmd
