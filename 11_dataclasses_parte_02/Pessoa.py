from dataclasses import dataclass
from abc import ABC
from abc import abstractmethod

@dataclass
@classmethod
class Pessoa(ABC):
    email: str
    telefone: str
    endereco: str