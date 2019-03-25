from django.urls import path

from calculation_app.views import MainView, SalesPanelView, ValuationPanelView, CalculationPanelView, ClientAddView, \
    ClientDetailView, ClientUpdateView, ClientDeleteView, AnnouncementsAddView, AnnouncementsEditView, AddContractView

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('client_list/', SalesPanelView.as_view(), name='client-list'),
    path('add_client/', ClientAddView.as_view(), name='add-client'),
    path('update_client/<int:pk>/', ClientUpdateView.as_view(), name='client-update'),
    path('delete_client/<int:pk>/', ClientDeleteView.as_view(), name='client-delete'),
    path('client/<int:client_id>/', ClientDetailView.as_view(), name='client-detail'),
    path('valuation_panel/', ValuationPanelView.as_view(), name='valuation-panel-view'),
    path('calculation_panel/', CalculationPanelView.as_view(), name='calculation-panel-view'),
    path('announcement_add/', AnnouncementsAddView.as_view(), name='announcement-add'),
    path('announcement_edit/<int:announcement_id>', AnnouncementsEditView.as_view(), name='announcement-edit'),
    path('add_contract/<int:client_id>/', AddContractView.as_view(), name='add-contract'),

]
