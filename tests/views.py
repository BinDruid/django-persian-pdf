from django_persian_pdf import views

from .models import Staff


class HTMLToTemplatePrint(views.HTMLToPDFTemplateView):
    template_name = 'staff.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['staffs'] = Staff.objects.all()
        return context


class HTMLToDetailPrint(views.HTMLToPDFDetailView):
    queryset = Staff.objects.all()
    template_name = 'staff_detail.html'


class LatexToTemplatePrint(views.LatexToPDFTemplateView):
    template_name = 'staff.tex'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['staffs'] = Staff.objects.all()
        return context


class LatexToDetailPrint(views.LatexToPDFDetailView):
    queryset = Staff.objects.all()
    template_name = 'staff_detail.tex'
