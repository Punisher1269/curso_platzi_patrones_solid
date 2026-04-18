from typing import Protocol
from schemas import PaymentResponse



class RefundPaymentProtocol(Protocol):
    def refund_payment(self, transaction_id: str) -> PaymentResponse: ...
