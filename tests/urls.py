from django.urls import path

from . import views

urlpatterns = [
    path('chrome/', views.ChromeTemplatePrint.as_view(), name='print-chrome-template'),
    path('chrome/<int:pk>/', views.ChromeTemplatePrint.as_view(), name='print-chrome-detail'),
    path('latex/', views.LatexTemplatePrint.as_view(), name='print-latex-template'),
    path('latex/<int:pk>/', views.LatexDetailPrint.as_view(), name='print-latex-detail'),
]
