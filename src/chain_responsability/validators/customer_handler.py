from .chain_handler import chain_handler
from .customer import CustomerValidator
from schemas import Request


class CustomerHandler(chain_handler):

    def handle(self, request: Request):
        validator = CustomerValidator()
        try:
            validator.validate(request.customer_data)
            if self._next_handler:
                self._next_handler.handle(request)
        except Exception as e:
            print("Errir")
            raise e
            
            
