from django.urls import path

from calculation_app.views import ClientListView, ClientAddView, ClientDetailView, ClientUpdateView, ClientDeleteView, \
    SubcontractorListView, SubcontractorDetailView, SubcontractorAddView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('clients/', ClientListView.as_view(), name='client-list'),
    path('client-detail/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),
    path('client-add/', ClientAddView.as_view(), name='client-add'),
    path('client-update/<int:pk>/', ClientUpdateView.as_view(), name='client-update'),
    path('client-delete/<int:pk>/', ClientDeleteView.as_view(), name='client-delete'),
    path('subcontractors/', SubcontractorListView.as_view(), name='subcontractor-list'),
    path('subcontractor-detail/<int:pk>/', SubcontractorDetailView.as_view(), name='subcontractor-detail'),
    path('subcontractor-add/', SubcontractorAddView.as_view(), name='subcontractor-add'),
    path('about/', views.about, name='calc-about'),
]
