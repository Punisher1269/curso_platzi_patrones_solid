from typing import Protocol
from schemas import CustomerData, PaymentResponse, PaymentData



class RecurringPaymentProtocol(Protocol):
    def setup_recurring_payment(
        self, customer_data: CustomerData, payment_data: PaymentData
    ) -> PaymentResponse: ...
