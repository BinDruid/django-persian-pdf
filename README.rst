Django Persian PDF
=========================

Django Persian PDF is a set of class based views allowing you to generate PDF reports
using html or latex templates.
Django Persian PDF under the hood uses two compiler to render template
and build the actual pdf file:

-  **Xelatex**
-  **Google Chrome**

Using this approach avoids regular overhead for parsing html tags, improving overall
response time and memory usage when generating large pdf files.
Django Persian PDF follows django class based views and base on the compilers provide 4 generic view classes.
The only difference is that these classes render their associated template and return a pdf file as response.
Just like django views you can pass queryset or make context to be used in template.
Here are the view classes available in **django_persian_pdf**:

-  ``HTMLToPDFTemplateView`` is an extension of django ``TemplateView`` using ``.html`` template to generate pdf file.
-  ``HTMLToPDFDetailView`` is an extension of django ``DetailView`` using ``.html`` template  to generate pdf file.
-  ``LatexToPDFTemplateView`` is an extension of django ``TemplateView`` using ``.tex`` template to generate pdf file.
-  ``LatexToPDFDetailView`` is an extension of django ``DetailView`` using ``.tex`` template to generate pdf file.

Status
------

.. image:: https://img.shields.io/github/actions/workflow/status/bindruid/django-persian-pdf/test.yml.svg?branch=master
   :target: https://github.com/bindruid/django-persian-pdf/actions?workflow=Test

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

- Make sure you have installed either ``google-chrome-stable`` or ``texlive-xetex`` on your machine.

.. code-block:: bash


   sudo apt install google-chrome-stable
   sudo apt install texlive-xetex

Usage
-----

1. Edit settings.py and add `django_persian_pdf` to your `INSTALLED_APPS`.

2. Inherit your views from appropriate Template or Detail view classes.

Example #1: Using HTML Template to generate a PDF response

.. code-block:: python

    from django_persian_pdf import views as pdf_views

    class TemplatePrint(pdf_views.HTMLToPDFTemplateView):
        template_name = 'payment_reports.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data()
            context['payments'] = Payments.objects.all()
            return context

    class DetailPrint(pdf_views.HTMLToPDFDetailView):
        template_name = 'payment_detail.html'
        queryset = Payments.objects.all()



Example #2: Using LaTeX Template to generate a PDF response

.. code-block:: python

    from django_persian_pdf import views as pdf_views

    class TemplatePrint(pdf_views.LatexToPDFTemplateView):
        template_name = 'payment_reports.tex'

        def get_context_data(self, **kwargs):
            context = super().get_context_data()
            context['payments'] = Payments.objects.all()
            return context

    class DetailPrint(pdf_views.LatexToPDFDetailView):
        template_name = 'payment_detail.tex'
        queryset = Payments.objects.all()

Notes on LaTeX
----------------

1. Using latex template with persian fonts requires you to have installed your persian fonts in home directory.

.. code-block:: bash


   mkdir ~/.fonts
   cp /path_to_fonts/Vazirmatn.ttf ~/.fonts/
   fc-cache -f -v

2. In latex template make sure you have used ``xepersian`` package as last package.

3. Define persian fonts in latex template.

4. You can use django template tags in latex template.

Here is an example of latex template for a given view:

.. code-block:: latex

    \documentclass[a4paper,9pt]{letter}
    \usepackage[portrait,margin=0.1in]{geometry}
    \usepackage{xepersian}

    \settextfont{Vazirmatn}
    \setlatintextfont{Vazirmatn}
    \setdigitfont[Scale=1.1]{Vazirmatn}


    \begin{document}

      {% for payment in payments %}
        {{ payment.trace_code }}
        \newline
        {{ payment.amount }}
        \newline
      {% endfor %}

    \end{document}

