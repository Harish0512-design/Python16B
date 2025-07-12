from abc import ABC
from typing import Optional


class BaseEntity(ABC):
    """
    Base class for all entities.
    Requires a method to get the primary ID.
    """

    def get_id(self) -> Optional[int]:
        raise NotImplementedError("Must implement get_id() in subclass.")
