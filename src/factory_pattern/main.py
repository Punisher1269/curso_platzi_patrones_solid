from src.factory_pattern.service import PaymentService
from .processors import StripePaymentProcessor


from notifiers import EmailNotifier, SMSNotifier, Notifier
from loggers import TransactionLogger
from schemas import CustomerData, ContactInfo, PaymentData
from validators import CustomerValidator, PaymentDataValidator


def get_email_notifier() -> EmailNotifier:
    return EmailNotifier()


def get_sms_notifier() -> SMSNotifier:
    return SMSNotifier(gateway="Test")


def get_notifier_implemetation(customer_data: CustomerData) -> Notifier:

    if customer_data.contact_info.phone:
        return SMSNotifier(gateway="SMSGetawayExample")

    if customer_data.contact_info.email:
        return EmailNotifier()

    raise ValueError("No se puede elegir la estategia correcta")


def get_customer_data() -> CustomerData:
    contact_into = ContactInfo(email="email@gmail.com")

    customer_data = CustomerData(name="David", contact_info=contact_into)

    return customer_data


if __name__ == "__main__":
    stripe_payment_procesor = StripePaymentProcessor()

    customer_data = get_customer_data()
    notifier = get_notifier_implemetation(customer_data)

    email_notifier = get_email_notifier()
    sms_notifier = get_sms_notifier()

    customer_validator = CustomerValidator()
    payment_data_validator = PaymentDataValidator()
    logger = TransactionLogger()

    payment_data = PaymentData(amount=100, source="tok_visa", currency="USD")
    service = PaymentService.create_with_payment_processor(
        payment_data=payment_data,
        notifier=notifier,
        customer_validator=customer_validator,
        payment_validator=payment_data_validator,
        logger=logger,
    )

    print(service)

    # service = PaymentService(
    #     payment_processor=stripe_payment_procesor,
    #     notifier=notifier,
    #     customer_validator=customer_validator,
    #     payment_validator=payment_data_validator,
    #     logger=logger,
    # )

    # # Cambio de estrategia de notificacion a estrategia de email
    # service.set_notifier(sms_notifier)

    # # Cambio de estrategia de notificacion a estrategia de email
    # service.set_notifier(email_notifier)