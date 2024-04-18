Django Persian PDF
=========================

Django Persian PDF is a set of class based views allowing you to generate PDF reports
using html or latex templates.
Django Persian PDF under the hood uses two compiler to render template
and build the actual pdf file:
-  Xelatex
-  Google Chrome

Using this approach avoids regular overhead for parsing html tags, improving overall
response time and memory usage when generating large pdf files.
Django Persian PDF follows django class based views and base on the compiler provide 4 generic view classes.
The only difference is that these classes render their associated template and return a pdf file as response.
Just like django views you can pass queryset or make context to be used in template.
Here are the view classes available in `django_persian_pdf`:

-  `ChromePDFTemplateView` is an extension of django `TemplateView` which uses chrome and .html template to generate pdf file.
-  `ChromePDFDetailView` is an extension of django `DetailView` which uses chrome and .html template  to generate pdf file.
-  `LatexPDFTemplateView` is an extension of django `TemplateView` which uses latex and .tex template to generate pdf file.
-  `LatexPDFDetailView` is an extension of django `DetailView` which uses latex to and .tex template to generate pdf file.

Status
------

.. image:: https://github.com/bindruid/django-persian-pdf/workflows/Test/badge.svg?branch=master
   :target: https://github.com/bindruid/django-persian-pdf/actions

.. image:: https://img.shields.io/pypi/v/django-persian-pdf.svg
   :target: https://pypi.python.org/pypi/django-persian-pdf

.. image:: https://img.shields.io/pypi/pyversions/django-persian-pdf.svg
   :target: https://pypi.org/project/django-persian-pdf

.. image:: https://img.shields.io/pypi/djversions/django-persian-pdf.svg
   :target: https://pypi.org/project/django-persian-pdf/

Dependencies
------------

-  Django >= 3.2
-  Google Chrome Stable
-  xelatex

Install
-------

.. code-block:: bash

   pip install django-persian-pdf

Usage
-----

0. Make sure you have installed either `chrome_stable_` or `xelatex` on your machine.

1. Edit settings.py and add `django_persian_pdf` to your `INSTALLED_APPS`.

2. Inherit your views from appropriate Template or Detail view classes.

.. code-block:: python

    from django_persian_pdf import views

    class TemplatePrint(views.ChromePDFTemplateView):
        template_name = 'payment_reports.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data()
            context['payments'] = Payments.objects.all()
            return context

    class DetailPrint(views.ChromePDFDetailView):
        template_name = 'payment_detail.html'
        queryset = Payments.objects.all()


.. code-block:: python

    from django_persian_pdf import views

    class TemplatePrint(views.LatexPDFTemplateView):
        template_name = 'payment_reports.tex'

        def get_context_data(self, **kwargs):
            context = super().get_context_data()
            context['payments'] = Payments.objects.all()
            return context

    class DetailPrint(views.LatexPDFDetailView):
        template_name = 'payment_detail.tex'
        queryset = Payments.objects.all()

3. Using latex template for persian requires you to have installed your persian fonts in home.

.. code-block:: bash


   mkdir -p ~/.fonts
   cp /path_to_fonts/Vazirmatn.ttf ~/.fonts/
   fc-cache -f -v
