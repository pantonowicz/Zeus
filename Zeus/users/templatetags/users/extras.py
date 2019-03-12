from django import template
from django.shortcuts import get_object_or_404
from calculation_app.models import SalesTeamMember, ValuationTeamMember

register = template.Library()


@register.filter()
def name_of_clients(sales):
    sales = get_object_or_404(SalesTeamMember, user_id=sales.id)
    clients = sales.clients
    if clients:
        return clients
    else:
        return "No clients assigned"


@register.filter()
def valuation_in_progres(evaluatior):
    evaluatior = get_object_or_404(ValuationTeamMember, user_id=evaluatior.id)
    valuation = evaluatior.evaluation

    if valuation:
        return valuation
    else:
        return "No evaluations assigned"
