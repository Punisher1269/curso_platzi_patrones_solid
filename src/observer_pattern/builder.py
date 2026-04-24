from typing import Optional, Self
from dataclasses import dataclass
from schemas import PaymentData, CustomerData
from src.builder_pattern.loggers.transaction import TransactionLogger
from src.builder_pattern.notifiers.email import EmailNotifier
from src.builder_pattern.notifiers.notifier import Notifier
from src.builder_pattern.notifiers.sms import SMSNotifier
from src.builder_pattern.processors.payment import PaymentProcessorProtocol
from src.builder_pattern.processors.recurring import RecurringPaymentProtocol
from src.builder_pattern.processors.refunds import RefundPaymentProtocol
from src.builder_pattern.service import PaymentService
from src.builder_pattern.validators.customer import CustomerValidator
from src.builder_pattern.validators.payment import PaymentDataValidator
from src.builder_pattern.factory import PaymentProcessorFactory
from listeners import ListenersManager, accountability_listener


@dataclass
class PaymentServiceBuilder :
    payment_processor: Optional[PaymentProcessorProtocol] = None
    notifier: Optional[Notifier] = None
    customer_validator: Optional[CustomerValidator] = None
    payment_validator: Optional[PaymentDataValidator] = None
    logger: Optional[TransactionLogger] = None
    listener = Optional[ListenersManager] = None
    recurring_processor: Optional[RecurringPaymentProtocol] = None
    refund_processor: Optional[RefundPaymentProtocol] = None


    def set_logger(self) -> Self:
        self.logger = TransactionLogger()
        return self
    

    def set_payment_validation(self) -> Self:
        self.payment_validator = PaymentDataValidator()
        return self
    

    def set_customer_validator(self) -> Self:
        self.customer_validator = CustomerValidator()
        return self
    

    def set_payment_processor(self, payment_data : PaymentData) -> Self:
        self.payment_processor = (
            PaymentProcessorFactory.create_payment_processor(payment_data)
        )
        return self
    

    def set_notifier(self, customer_data : CustomerData) -> Self:
        if customer_data.contact_info.email:
            self.notifier = EmailNotifier()
            return self
        if customer_data.contact_info.phone:
            self.notifier = SMSNotifier()
            return self

        raise ValueError("No se puede seleccionar clase de notificacion")


    def set_listeners(self):
        listener = ListenersManager()
        accountability = accountability_listener()
        listener.add(accountability)

        self.listener = listener
        

    def build(self):
        if not all(
            [
                self.payment_processor,
                self.notifier,
                self.customer_validator,
                self.payment_validator,
                self.logger,
                self.listener
            ]
        ):
            missing = [
                name
                for name, value in [
                    ("payment_procesor", self.payment_processor),
                    ("notifier", self.notifier),
                    ("customer_validator", self.customer_validator),
                    ("payment_validator", self.payment_validator),
                    ("logger", self.logger)
                    ("listener", self.listener)
                ]
                if value is None
            ]     

            raise ValueError(f"Missing Dependecies : {missing} ")   

        return PaymentService(
            payment_processor=self.payment_processor,
            payment_validator=self.payment_validator,
            customer_validator=self.customer_validator,
            notifier=self.notifier,
            logger=self.logger,
            listener=self.listener 
        )
    
    

 