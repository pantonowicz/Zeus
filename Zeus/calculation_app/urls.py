from django.urls import path

from calculation_app.views import ClientListView, ClientAddView, ClientDetailView, ClientUpdateView, ClientDeleteView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('clients/', ClientListView.as_view(), name='client-list'),
    path('client-detail/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),
    path('add-client/', ClientAddView.as_view(), name='add-client'),
    path('client-update/<int:pk>/', ClientUpdateView.as_view(), name='client-update'),
    path('client-delete/<int:pk>/', ClientDeleteView.as_view(), name='client-delete'),
    path('about/', views.about, name='calc-about'),
]
