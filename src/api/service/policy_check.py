from enum import Enum
from ..storage.credit_policy import CreditPolicy

class Result(str, Enum):
    ACCEPT = "ACCEPT"
    LOW_INCOME = "LOW_INCOME"
    HIGH_DEBT_FOR_INCOME = "HIGH_DEBT_FOR_INCOME"
    PAYMENT_REMARKS_12M = "PAYMENT_REMARKS_12M"
    PAYMENT_REMARKS = "PAYMENT_REMARKS"
    UNDERAGE = "UNDERAGE"

def checkPolicy(creditPolicy: CreditPolicy):
    if creditPolicy.customer_income < 500:
        return Result("LOW_INCOME").value
    elif creditPolicy.customer_debt > (creditPolicy.customer_income / 2):
        return Result("HIGH_DEBT_FOR_INCOME").value
    elif creditPolicy.payment_remarks_12m > 0:
        return Result("PAYMENT_REMARKS_12M").value
    elif creditPolicy.payment_remarks > 1:
        return Result("PAYMENT_REMARKS").value
    elif creditPolicy.customer_age < 18:
        return Result("UNDERAGE").value
    else:
        return Result("ACCEPT").value