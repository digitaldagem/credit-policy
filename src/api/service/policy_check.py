from enum import Enum
from ..storage.credit_policy import CreditPolicy

class Result(Enum):
    ACCEPT = 1
    LOW_INCOME = 2
    HIGH_DEBT_FOR_INCOME = 3
    PAYMENT_REMARKS_12M = 4
    PAYMENT_REMARKS = 5
    UNDERAGE = 6

def checkPolicy(creditPolicy: CreditPolicy):
    if creditPolicy.customer_income < 500:
        return Result(2).name
    elif creditPolicy.customer_debt > (creditPolicy.customer_income / 2):
        return Result(3).name
    elif creditPolicy.payment_remarks_12m > 0:
        return Result(4).name
    elif creditPolicy.payment_remarks > 1:
        return Result(5).name
    elif creditPolicy.customer_age < 18:
        return Result(6).name
    else:
        return Result(1).name