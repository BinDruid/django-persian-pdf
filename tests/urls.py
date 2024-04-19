from django.urls import path

from . import views

urlpatterns = [
    path('chrome/', views.HTMLToTemplatePrint.as_view(), name='print-chrome-template'),
    path('chrome/<int:pk>/', views.HTMLToTemplatePrint.as_view(), name='print-chrome-detail'),
    path('latex/', views.LatexToTemplatePrint.as_view(), name='print-latex-template'),
    path('latex/<int:pk>/', views.LatexToDetailPrint.as_view(), name='print-latex-detail'),
]
