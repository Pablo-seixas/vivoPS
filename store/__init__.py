# usecases/__init__.py

from abc import ABC, abstractmethod
from typing import Any, Dict


class UseCase(ABC):
    @abstractmethod
    def execute(self, request: Dict[str, Any]) -> Any:
        pass


class UseCaseFactory:
    def create_use_case(self, name: str) -> UseCase:
        if name == "CreateProductUseCase":
            return CreateProductUseCase()
        elif name == "GetProductUseCase":
            return GetProductUseCase()
        # Adicione mais casos de uso conforme necessário
        else:
            raise ValueError("Use case not found")


class CreateProductUseCase(UseCase):
    def execute(self, request: Dict[str, Any]) -> Any:
        # Lógica para criar um produto
        pass


class GetProductUseCase(UseCase):
    def execute(self, request: Dict[str, Any]) -> Any:
        # Lógica para obter um produto
        pass
