from django.db import models

SEGMENTS_CHOICES = (
    ('1', 'AUTOMOTIVE, TRANSPORT & AERONAUTIC'),
    ('2', 'CHEMICAL & PHARMACEUTICAL'),
    ('3', 'CONSTRUCTION, DECONSTRUCTION & MATERIALS '),
    ('4', 'ELECTRONIC AND ELECTRIC PRODUCTS'),
    ('5', 'ENVIRONMENTAL SERVICES'),
    ('6', 'FOOD AND BEVERAGE'),
    ('7', 'HEALTHCARE AND SOCIAL WORK ACTIVITIES'),
    ('8', 'MINING & QUARRYING'),
    ('9', 'OIL & GAS'),
    ('10', 'OTHER MANUFACTURING'),
    ('11', 'PRIVATE SERVICES'),
    ('12', 'PULP & PAPER'),
    ('13', 'TRANSPORTATION & STORAGE'),
    ('14', 'WHOLESALE, RETAIL TRADE'),
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


class Subcontractors(models.Model):
    """Dane dotyczące podwykonawców"""
    name = models.CharField(max_length=128, null=False)
    city = models.CharField(max_length=64)
    postal = models.CharField(max_length=32)
    street = models.CharField(max_length=128)
    nip = models.DecimalField(max_digits=10, decimal_places=0)
    waste_code = models.ManyToManyField(WasteCodes)

    def __str__(self):
        return f'Subcontractor: {self.name}, From: {self.street}, {self.postal} {self.city}'


class Calculation(models.Model):
    """Dane dotyczące kontraktu"""
    contract_duration = models.DateField()
    payment_deadline = models.SmallIntegerField()
    offer_deadline = models.DateField()
    date_created = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)



class MassWaste(models.Model):
    waste_mass = models.DecimalField(max_digits=9, decimal_places=2)
    waste_codes = models.ForeignKey(WasteCodes, on_delete=models.CASCADE)
    calculation = models.ForeignKey(Calculation, on_delete=models.CASCADE)


class Order(models.Model):
    """Dane dotyczące wyliczeń"""
    subcontractor = models.ForeignKey(Subcontractors, on_delete=models.CASCADE)
    calculation = models.OneToOneField(MassWaste, on_delete=models.CASCADE)
    local_transport_cost = models.DecimalField(max_digits=9, decimal_places=2)
    instalation_transport_cost = models.DecimalField(max_digits=9, decimal_places=2)
    management_cost = models.DecimalField(max_digits=9, decimal_places=2)
    logistic_details = models.CharField(max_length=256)
    quality_details = models.CharField(max_length=256)
    unit = models.CharField(max_length=32)
    costs_mg = models.DecimalField(max_digits=9, decimal_places=2)
    margin_mg = models.DecimalField(max_digits=9, decimal_places=2)
    turnover = models.DecimalField(max_digits=12, decimal_places=2)
    total_costs = models.DecimalField(max_digits=12, decimal_places=2)
