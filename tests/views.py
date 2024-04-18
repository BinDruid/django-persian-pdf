from django_persian_pdf import views
from .models import Staff


class ChromeTemplatePrint(views.ChromePDFTemplateView):
    template_name = 'staff.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['staffs'] = Staff.objects.all()
        return context


class ChromeDetailPrint(views.ChromePDFDetailView):
    queryset = Staff.objects.all()
    template_name = 'staff_detail.html'


class LatexTemplatePrint(views.LatexPDFTemplateView):
    template_name = 'staff.tex'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['staffs'] = Staff.objects.all()
        return context


class LatexDetailPrint(views.LatexPDFDetailView):
    queryset = Staff.objects.all()
    template_name = 'staff_detail.tex'
