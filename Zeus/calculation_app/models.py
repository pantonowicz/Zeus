from django.db import models
from django.contrib.auth.models import User

SEGMENTS_CHOICES = (
    (1, 'AUTOMOTIVE, TRANSPORT & AERONAUTIC'),
    (2, 'CHEMICAL & PHARMACEUTICAL'),
    (3, 'CONSTRUCTION, DECONSTRUCTION & MATERIALS '),
    (4, 'ELECTRONIC AND ELECTRIC PRODUCTS'),
    (5, 'ENVIRONMENTAL SERVICES'),
    (6, 'FOOD AND BEVERAGE'),
    (7, 'HEALTHCARE AND SOCIAL WORK ACTIVITIES'),
    (8, 'MINING & QUARRYING'),
    (9, 'OIL & GAS'),
    (10, 'OTHER MANUFACTURING'),
    (11, 'PRIVATE SERVICES'),
    (12, 'PULP & PAPER'),
    (13, 'TRANSPORTATION & STORAGE'),
    (14, 'WHOLESALE, RETAIL TRADE'),
)

WASTE_PERMISSION_CHOICES = [
    (0, "Gathering wastes"),
    (1, "Generating wastes"),
    (2, "Processing wastes"),
    (3, "Transporting wastes"),
]

UNIT_CHOICES = (
    (1, 'PLN/Mg'),
    (2, 'PLN/course'),
    (3, 'PLN/container'),
)

EQUIPMENT = (
    (1, '240l bin'),
    (2, '1100l bin'),
    (3, 'Container 7m'),
    (4, 'Container 20m'),
    (5, 'Container 34m'),
    (6, 'Barrel'),
    (7, '1000l DPPL'),
    (8, 'EURO-Pallets'),
)


class WasteCodes(models.Model):
    code = models.CharField(max_length=32)
    description = models.TextField()

    def __str__(self):
        return f'{self.code} - {self.description}'


# class Bdo(models.Model):
#     """lista klientów z numerem bdo"""
#     bdo_number = models.DecimalField(max_digits=9, decimal_places=0)
#     company = models.CharField(max_length=128)
#     nip = models.DecimalField(max_digits=10, decimal_places=0)
#
#     def __str__(self):
#         return f'Client: {self.company} - {self.bdo_number}'

class SalesTeamMember(models.Model):
    """Model handlowca i przypisanych tematów"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class ValuationTeamMember(models.Model):
    """Model działu wycen"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class CalculationTeamMember(models.Model):
    """Model działu kalkulacji"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Client(models.Model):
    """Dane dotyczące klienta"""
    sales_rep = models.ForeignKey(SalesTeamMember, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, null=False)
    segment = models.IntegerField(choices=SEGMENTS_CHOICES)
    city = models.CharField(max_length=64)
    postal = models.CharField(max_length=32)
    street = models.CharField(max_length=128)
    nip = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return f'Client: {self.name}, Segment: {self.segment}, From: {self.street}, {self.postal} {self.city}'


class Subcontractor(models.Model):
    """Dane dotyczące podwykonawców"""
    name = models.CharField(max_length=128, null=False)
    city = models.CharField(max_length=64)
    postal = models.CharField(max_length=32)
    street = models.CharField(max_length=128)
    nip = models.DecimalField(max_digits=10, decimal_places=0)
    person = models.CharField(max_length=32)
    phone = models.CharField(max_length=16)
    email = models.EmailField()

    # waste_code = models.ManyToManyField(WasteCodes)

    def __str__(self):
        return f'Subcontractor: {self.name}, From: {self.street}, {self.postal} {self.city}'


class WasteCodeSubcontractor(models.Model):
    subcontractor = models.ForeignKey(Subcontractor, on_delete=models.CASCADE)
    waste_code = models.ForeignKey(WasteCodes, on_delete=models.CASCADE)
    permission = models.IntegerField(choices=WASTE_PERMISSION_CHOICES)

    def __str__(self):
        return f'{self.subcontractor} - {self.waste_code} -{self.permission}'


class ContractDetails(models.Model):
    """Dane dotyczące kontraktu"""
    sales_rep = models.ForeignKey(SalesTeamMember, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    contract_duration = models.CharField(max_length=16)
    payment_deadline = models.SmallIntegerField()
    offer_deadline = models.DateField()
    date_created = models.DateTimeField(auto_now_add=True)
    info = models.TextField()
    contact_person = models.CharField(max_length=32)
    contact_phone = models.CharField(max_length=16)
    contact_email = models.EmailField()

    def __str__(self):
        return f'{self.sales_rep.client_set} - offer deadline by {self.offer_deadline}'


class MassWaste(models.Model):
    contract_details = models.ForeignKey(ContractDetails, on_delete=models.CASCADE)
    waste_codes = models.ForeignKey(WasteCodes, on_delete=models.CASCADE)
    waste_mass = models.DecimalField(max_digits=9, decimal_places=2)
    additional_info = models.CharField(max_length=32)

    def __str__(self):
        return f'Codes: {self.waste_codes}, Mass: {self.waste_mass}'


class Evaluation(models.Model):
    """Dane dotyczące kosztu"""
    evaluation_employee = models.ManyToManyField(ValuationTeamMember)
    subcontractor = models.ManyToManyField(Subcontractor)
    mass_waste = models.OneToOneField(MassWaste, on_delete=models.CASCADE)
    transport_cost = models.DecimalField(max_digits=9, decimal_places=2)
    management_cost = models.DecimalField(max_digits=9, decimal_places=2)
    containter = models.CharField(choices=EQUIPMENT, max_length=32)
    logistic_details = models.CharField(max_length=256)
    quality_details = models.CharField(max_length=256)
    unit = models.CharField(UNIT_CHOICES, max_length=32)
    costs_mg = models.DecimalField(max_digits=9, decimal_places=2)
    evaluated = models.BooleanField(default=False)


class Calculation(models.Model):
    calculation_employee = models.ManyToManyField(CalculationTeamMember)
    calc_cost = models.ForeignKey(Evaluation, on_delete=models.CASCADE)
    costs_per_mg = models.DecimalField(max_digits=9, decimal_places=2)
    margin_per_mg = models.DecimalField(max_digits=9, decimal_places=2)
    price_per_mg = models.DecimalField(max_digits=9, decimal_places=2)
    margin = models.DecimalField(max_digits=9, decimal_places=2)
    turnover = models.DecimalField(max_digits=12, decimal_places=2)
    total_costs = models.DecimalField(max_digits=12, decimal_places=2)
    calculated = models.BooleanField(default=False)


class Announcements(models.Model):
    title = models.CharField(max_length=64)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
