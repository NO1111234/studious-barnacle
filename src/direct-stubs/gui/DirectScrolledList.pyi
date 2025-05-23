__all__ = ['DirectScrolledList', 'DirectScrolledListItem']

from collections.abc import Callable, Iterable, Sequence
from typing import Any, ClassVar, Literal
from typing_extensions import TypeAlias, Unpack

from direct.directnotify.Notifier import Notifier
from panda3d.core import NodePath

from ._typing import ButtonKeywords, FrameKeywords, PGItemT
from .DirectButton import DirectButton
from .DirectFrame import DirectFrame

_TextProperties_Alignment: TypeAlias = Literal[0, 1, 2, 3, 4, 5]

class DirectScrolledListItem(DirectButton):
    notify: ClassVar[Notifier]
    def __init__(self, parent: NodePath | None = None, **kw: Unpack[ButtonKeywords]) -> None: ...
    def select(self) -> None: ...

class DirectScrolledList(DirectFrame[PGItemT]):
    notify: ClassVar[Notifier]
    index: int
    nextItemID: int
    incButton: DirectButton
    decButton: DirectButton
    itemFrame: DirectFrame
    currentSelected: DirectScrolledListItem
    def __init__(
        self,
        parent: NodePath | None = None,
        *,
        pgFunc: Callable[[str], PGItemT] = ...,
        items: Sequence[DirectFrame | str] = ...,
        itemsAlign: _TextProperties_Alignment = 2,
        itemsWordwrap=None,
        command: Callable[..., object] | None = None,
        extraArgs: Iterable[Any] = ...,
        itemMakeFunction: Callable[[str, int, Any], DirectFrame] | None = None,
        itemMakeExtraArgs: Any = ...,
        numItemsVisible: int = 1,
        scrollSpeed: float = 8,
        forceHeight: float | None = None,
        incButtonCallback: Callable[[], object] | None = None,
        decButtonCallback: Callable[[], object] | None = None,
        **kw: Unpack[FrameKeywords],
    ) -> None: ...
    def setForceHeight(self) -> None: ...
    def recordMaxHeight(self) -> None: ...
    def setScrollSpeed(self) -> None: ...
    def setNumItemsVisible(self) -> None: ...
    def selectListItem(self, item: DirectScrolledListItem) -> None: ...
    def scrollBy(self, delta: int) -> None: ...
    def getItemIndexForItemID(self, itemID: int) -> int: ...
    def scrollToItemID(self, itemID: int, centered: bool = ...) -> None: ...
    def scrollTo(self, index: int, centered: bool = ...) -> bool: ...
    def makeAllItems(self) -> None: ...
    def addItem(self, item: DirectScrolledListItem | str, refresh: bool = ...) -> None: ...
    def removeItem(self, item: DirectScrolledListItem | str, refresh: bool = ...) -> bool: ...
    def removeAndDestroyItem(self, item: DirectScrolledListItem, refresh: bool = ...) -> bool: ...
    def removeAllItems(self, refresh: bool = ...) -> bool: ...
    def removeAndDestroyAllItems(self, refresh: bool = ...) -> bool: ...
    def refresh(self) -> None: ...
    def getSelectedIndex(self) -> int: ...
    def getSelectedText(self) -> str: ...
    def setIncButtonCallback(self) -> None: ...
    def setDecButtonCallback(self) -> None: ...
