from typing import Optional
from dataclasses import dataclass
from src.builder_pattern.loggers.transaction import TransactionLogger
from src.builder_pattern.notifiers.notifier import Notifier
from src.builder_pattern.processors.payment import PaymentProcessorProtocol
from src.builder_pattern.processors.recurring import RecurringPaymentProtocol
from src.builder_pattern.processors.refunds import RefundPaymentProtocol
from src.builder_pattern.validators.customer import CustomerValidator
from src.builder_pattern.validators.payment import PaymentDataValidator


@dataclass
class PaymentServiceBuilder :
    payment_processor: Optional[PaymentProcessorProtocol] = None
    notifier: Optional[Notifier] = None
    customer_validator: Optional[CustomerValidator] = None
    payment_validator: Optional[PaymentDataValidator] = None
    logger: Optional[TransactionLogger] = None
    recurring_processor: Optional[RecurringPaymentProtocol] = None
    refund_processor: Optional[RefundPaymentProtocol] = None