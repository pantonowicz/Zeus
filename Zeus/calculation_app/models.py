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
    (3, 'PLN/caontainer'),
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

class SalesRepresentative(models.Model):
    """Model handlowca i przypisanych tematów"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    clients = models.ForeignKey('Clients', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Clients(models.Model):
    """Dane dotyczące klienta"""
    name = models.CharField(max_length=128, null=False)
    segment = models.CharField(choices=SEGMENTS_CHOICES, max_length=64)
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


class WasteCodeSubcotractor(models.Model):
    subcontractor = models.ForeignKey(Subcontractor, on_delete=models.CASCADE)
    waste_code = models.ForeignKey(WasteCodes, on_delete=models.CASCADE)
    permission = models.IntegerField(choices=WASTE_PERMISSION_CHOICES)

    def __str__(self):
        return f'{self.subcontractor} - {self.waste_code} -{self.permission}'


class ContractDetails(models.Model):
    """Dane dotyczące kontraktu"""
    sales_rep = models.ForeignKey(SalesRepresentative, on_delete=models.CASCADE)
    contract_duration = models.CharField(max_length=16)
    payment_deadline = models.SmallIntegerField()
    offer_deadline = models.DateField()
    date_created = models.DateTimeField(auto_now_add=True)
    info = models.TextField()
    contact_person = models.CharField(max_length=32)
    contact_phone = models.CharField(max_length=16)
    contact_email = models.EmailField()

    # client = models.ForeignKey(Clients, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.sales_rep.clients.name} - offer deadline by {self.offer_deadline}'


class MassWaste(models.Model):
    contract_details = models.ForeignKey(ContractDetails, on_delete=models.CASCADE)
    waste_codes = models.ForeignKey(WasteCodes, on_delete=models.CASCADE)
    waste_mass = models.DecimalField(max_digits=9, decimal_places=2)
    additional_info = models.CharField(max_length=32)

    def __str__(self):
        return f'Codes: {self.waste_codes}, Mass: {self.waste_mass}'


class Evaluation(models.Model):
    """Dane dotyczące wyliczeń"""
    subcontractor = models.ForeignKey(ContractDetails, on_delete=models.CASCADE)
    calculation = models.OneToOneField(MassWaste, on_delete=models.CASCADE)
    transport_cost = models.DecimalField(max_digits=9, decimal_places=2)
    management_cost = models.DecimalField(max_digits=9, decimal_places=2)
    containter = models.CharField(choices=EQUIPMENT, max_length=32)
    logistic_details = models.CharField(max_length=256)
    quality_details = models.CharField(max_length=256)
    unit = models.CharField(UNIT_CHOICES, max_length=32)
    costs_mg = models.DecimalField(max_digits=9, decimal_places=2)


class Calculation(models.Model):
    costs = models.ForeignKey(Evaluation, on_delete=models.CASCADE)
    costs_per_mg = models.DecimalField(max_digits=9, decimal_places=2)
    margin_per_mg = models.DecimalField(max_digits=9, decimal_places=2)
    price_per_mg = models.DecimalField(max_digits=9, decimal_places=2)
    margin = models.DecimalField(max_digits=9, decimal_places=2)
    turnover = models.DecimalField(max_digits=12, decimal_places=2)
    total_costs = models.DecimalField(max_digits=12, decimal_places=2)
