from django.template import Context, Template
from django.template.loader import get_template
from django.utils.encoding import smart_str
from django.views.generic.base import TemplateView
from django.views.generic.detail import SingleObjectMixin

from .compilers import ChromeCompiler, LatexCompiler
from .responses import PDFResponse


class PDFTemplateView(TemplateView):
    response_class = PDFResponse
    compiler_class = None

    def render_to_response(self, context, **response_kwargs):
        return self.render_to_pdf(context)

    def render_to_pdf(self, context):
        raw_template = self.render_template_file(context)
        pdf_file = self.compiler_class(raw_template).compile()
        return self.response_class(pdf_file)

    def render_template_file(self, context):
        template_content = self._read_template_file()
        build_context = Context(context)
        build_template = Template(template_content).render(build_context)
        return smart_str(build_template)

    def _read_template_file(self):
        template = get_template(self.template_name)
        template_path = template.origin.name
        with open(template_path) as f:
            content = f.read()
            return content


class PDFDetailView(SingleObjectMixin, PDFTemplateView):
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class LatexToPDFTemplateView(PDFTemplateView):
    compiler_class = LatexCompiler


class LatexToPDFDetailView(PDFDetailView):
    compiler_class = LatexCompiler


class HTMLToPDFTemplateView(PDFTemplateView):
    compiler_class = ChromeCompiler


class HTMLToPDFDetailView(PDFDetailView):
    compiler_class = ChromeCompiler
