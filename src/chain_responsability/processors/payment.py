from typing import Protocol
from schemas import CustomerData, PaymentResponse, PaymentData


class PaymentProcessorProtocol(Protocol):
    """
    Protocol for processing payments, refunds, and recurring payments.

    This protocol defines the interface for payment processors. Implementations
    should provide methods for processing payments, refunds, and setting up recurring payments.
    """

    def process_transaction(
        self, customer_data: CustomerData, payment_data: PaymentData
    ) -> PaymentResponse: ...
