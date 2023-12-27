from django.db import models

class CreditPolicy(models.Model):
    customer_income = models.IntegerField()
    customer_debt = models.IntegerField()
    payment_remarks_12m = models.IntegerField()
    payment_remarks = models.IntegerField()
    customer_age =  models.IntegerField()
