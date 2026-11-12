from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List, Optional
from oops.student_management_system.src.entities import BaseEntity

# T must be a subclass of BaseEntity and T can be of any type.
T = TypeVar('T', bound=BaseEntity)


class IRepository(ABC, Generic[T]):
    """
        Generic repository interface for any entity type.
    """

    # ... is like pass keyword
    @abstractmethod
    def add(self, obj: T) -> None: ...

    # Optional[T] means value can be either T or None.
    @abstractmethod
    def get_by_id(self, entity_id: int) -> Optional[T]: ...

    @abstractmethod
    def get_all(self) -> List[T]: ...

    @abstractmethod
    def update(self, obj: T) -> bool: ...

    @abstractmethod
    def delete(self, entity_id: int) -> bool: ...