from django.urls import path

from calculation_app.views import ClientListView, ClientAddView, ClientDetailView, ClientUpdateView, ClientDeleteView, \
    SubcontractorListView, SubcontractorDetailView, SubcontractorAddView, SubcontractorUpdateView, \
    SubcontractorDeleteView, CalculationAddView, CalculationDetailView, CalculationListView, CalculationUpdateView, \
    CalculationDeleteView, CalculationCodeAddView, CalculationCodeDeleteView, CostAddToCodeView
from . import views

urlpatterns = [
    # path('', views.home, name='home'),

    path('clients/', ClientListView.as_view(), name='client-list'),
    path('client-detail/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),
    path('client-add/', ClientAddView.as_view(), name='client-add'),
    path('client-update/<int:pk>/', ClientUpdateView.as_view(), name='client-update'),
    path('client-delete/<int:pk>/', ClientDeleteView.as_view(), name='client-delete'),

    path('subcontractors/', SubcontractorListView.as_view(), name='subcontractor-list'),
    path('subcontractor-detail/<int:pk>/', SubcontractorDetailView.as_view(), name='subcontractor-detail'),
    path('subcontractor-add/', SubcontractorAddView.as_view(), name='subcontractor-add'),
    path('subcontractor-update/<int:pk>/', SubcontractorUpdateView.as_view(), name='subcontractor-update'),
    path('subcontractor-delete/<int:pk>/', SubcontractorDeleteView.as_view(), name='subcontractor-delete'),

    path('calculation-list/', CalculationListView.as_view(), name='calculation-list'),
    path('calculation-detail/<int:pk>/', CalculationDetailView.as_view(), name='calculation-detail'),
    path('calculation-add/', CalculationAddView.as_view(), name='calculation-add'),
    path('calculation-update/<int:pk>', CalculationUpdateView.as_view(), name='calculation-update'),
    path('calculation-delete/<int:pk>/', CalculationDeleteView.as_view(), name='calculation-delete'),

    path('code-add/', CalculationCodeAddView.as_view(), name='code-add'),
    path('code-delete/<int:pk>', CalculationCodeDeleteView.as_view(), name='code-delete'),

    path('add-cost/<int:waste_code_id>', CostAddToCodeView.as_view(), name='add-cost'),

    # path('about/', views.about, name='calc-about'),
]
