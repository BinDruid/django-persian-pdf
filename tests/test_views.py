import mimetypes
import tempfile

from django.test import TestCase
from django.urls import reverse

from .models import Staff


class TestChromeTemplateView(TestCase):

    @classmethod
    def setUpTestData(cls):
        Staff.objects.bulk_create(
            [
                Staff(first_name='علی', last_name='محمدی', salary=2500, role='C'),
                Staff(first_name='حسن', last_name='طاهری', salary=1200, role='E'),
                Staff(first_name='محمد', last_name='اصغری', salary=1800, role='M'),
            ]
        )

    def test_get_chrome_generated_page_results_status_ok(self):
        # Arrange
        url = reverse('print-chrome-template')
        # Act
        response = self.client.get(url)
        # Assert
        value_under_test = response.status_code
        value_expected = 200
        self.assertEqual(value_under_test, value_expected, msg=f'Did not get the page')

    def test_get_chrome_generated_page_results_actual_pdf_file(self):
        # Arrange + Act
        url = reverse('print-chrome-template')
        response = self.client.get(url)
        # Assert
        value_under_test = response['Content-Type']
        value_expected = 'application/pdf'
        self.assertEqual(value_under_test, value_expected, msg='There was not a pdf file in header')
        with tempfile.NamedTemporaryFile(suffix='.pdf', mode='wb') as temp_file:
            temp_file.write(response.content)
            file_path = temp_file.name
            mime_type, encoding = mimetypes.guess_type(file_path)
            extension = mimetypes.guess_extension(mime_type)
            value_under_test = extension
            value_expected = '.pdf'
            self.assertEqual(value_under_test, value_expected, msg='File was not with pdf extension')


class TestChromeDetailView(TestCase):

    @classmethod
    def setUpTestData(cls):
        Staff.objects.create(first_name='علی', last_name='محمدی', salary=2500, role='C')

    def test_get_chrome_generated_page_results_status_ok(self):
        # Arrange
        url = reverse('print-chrome-detail', args=[1])
        # Act
        response = self.client.get(url)
        # Assert
        value_under_test = response.status_code
        value_expected = 200
        self.assertEqual(value_under_test, value_expected, msg=f'Did not get the page')

    def test_get_chrome_generated_page_results_actual_pdf_file(self):
        # Arrange + Act
        url = reverse('print-chrome-detail', args=[1])
        response = self.client.get(url)
        # Assert
        value_under_test = response['Content-Type']
        value_expected = 'application/pdf'
        self.assertEqual(value_under_test, value_expected, msg='There was not a pdf file in header')
        with tempfile.NamedTemporaryFile(suffix='.pdf', mode='wb') as temp_file:
            temp_file.write(response.content)
            file_path = temp_file.name
            mime_type, encoding = mimetypes.guess_type(file_path)
            extension = mimetypes.guess_extension(mime_type)
            value_under_test = extension
            value_expected = '.pdf'
            self.assertEqual(value_under_test, value_expected, msg='File was not with pdf extension')


class TestLatexTemplateView(TestCase):

    @classmethod
    def setUpTestData(cls):
        Staff.objects.bulk_create(
            [
                Staff(first_name='علی', last_name='محمدی', salary=2500, role='C'),
                Staff(first_name='حسن', last_name='طاهری', salary=1200, role='E'),
                Staff(first_name='محمد', last_name='اصغری', salary=1800, role='M'),
            ]
        )

    def test_get_latex_generated_page_results_status_ok(self):
        # Arrange
        url = reverse('print-latex-template')
        # Act
        response = self.client.get(url)
        # Assert
        value_under_test = response.status_code
        value_expected = 200
        self.assertEqual(value_under_test, value_expected, msg=f'Did not get the page')

    def test_get_latex_generated_page_results_actual_pdf_file(self):
        # Arrange + Act
        url = reverse('print-latex-template')
        response = self.client.get(url)
        # Assert
        value_under_test = response['Content-Type']
        value_expected = 'application/pdf'
        self.assertEqual(value_under_test, value_expected, msg='There was not a pdf file in header')
        with tempfile.NamedTemporaryFile(suffix='.pdf', mode='wb') as temp_file:
            temp_file.write(response.content)
            file_path = temp_file.name
            mime_type, encoding = mimetypes.guess_type(file_path)
            extension = mimetypes.guess_extension(mime_type)
            value_under_test = extension
            value_expected = '.pdf'
            self.assertEqual(value_under_test, value_expected, msg='File was not with pdf extension')


class TestLatexDetailView(TestCase):

    @classmethod
    def setUpTestData(cls):
        Staff.objects.create(first_name='علی', last_name='محمدی', salary=2500, role='C')

    def test_get_latex_generated_page_results_status_ok(self):
        # Arrange
        url = reverse('print-latex-detail', args=[1])
        # Act
        response = self.client.get(url)
        # Assert
        value_under_test = response.status_code
        value_expected = 200
        self.assertEqual(value_under_test, value_expected, msg=f'Did not get the page')

    def test_get_latex_generated_page_results_actual_pdf_file(self):
        # Arrange + Act
        url = reverse('print-latex-detail', args=[1])
        response = self.client.get(url)
        # Assert
        value_under_test = response['Content-Type']
        value_expected = 'application/pdf'
        self.assertEqual(value_under_test, value_expected, msg='There was not a pdf file in header')
        with tempfile.NamedTemporaryFile(suffix='.pdf', mode='wb') as temp_file:
            temp_file.write(response.content)
            file_path = temp_file.name
            mime_type, encoding = mimetypes.guess_type(file_path)
            extension = mimetypes.guess_extension(mime_type)
            value_under_test = extension
            value_expected = '.pdf'
            self.assertEqual(value_under_test, value_expected, msg='File was not with pdf extension')
