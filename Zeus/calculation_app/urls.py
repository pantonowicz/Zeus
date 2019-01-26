from django.urls import path

from calculation_app.views import ClientListView, ClientAddView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('clients/', ClientListView.as_view(), name='client-list'),
    path('add-client/', ClientAddView.as_view(), name='add-client'),
    path('about/', views.about, name='calc-about'),
]