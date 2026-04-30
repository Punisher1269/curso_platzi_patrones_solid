from abc import ABC, abstractclassmethod
from typing import Self, Optional
from dataclasses import dataclass
from schemas import Request


@dataclass
class chain_handler(ABC):

    _next_handler : Optional[Self] = None

    def set_next(self, handler : Self):
        self._next_handler = handler
        return handler 
    
    @abstractclassmethod
    def handle(self, request : Request):
        ...