from rest_framework import serializers
from .credit_policy import CreditPolicy

class CreditPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditPolicy
        fields = ['id', 'customer_income', 'customer_debt', 'payment_remarks_12m', 'payment_remarks', 'customer_age']
    