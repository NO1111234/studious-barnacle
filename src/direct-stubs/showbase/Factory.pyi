__all__ = ['Factory']

from _typeshed import Unused
from typing import Any, ClassVar

from direct.directnotify.Notifier import Notifier

class Factory:
    notify: ClassVar[Notifier]
    def __init__(self) -> None: ...
    def create(self, type: type, *args: Any, **kwArgs: Any) -> Any: ...
    def nullCtor(self, *args: Unused, **kwArgs: Unused) -> None: ...
