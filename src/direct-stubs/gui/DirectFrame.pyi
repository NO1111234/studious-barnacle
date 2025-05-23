__all__ = ['DirectFrame']

from collections.abc import Callable, Sequence
from typing import ClassVar, Literal
from typing_extensions import Unpack

from panda3d.core import NodePath

from ._typing import FrameKeywords, MaybeGeomOrSequence, MaybeImageOrSequence, PGItemT
from .DirectGuiBase import DirectGuiWidget

class DirectFrame(DirectGuiWidget[PGItemT]):
    DefDynGroups: ClassVar[tuple[Literal['text'], Literal['geom'], Literal['image']]]
    def __init__(
        self, parent: NodePath | None = None, *, pgFunc: Callable[[str], PGItemT] = ..., **kw: Unpack[FrameKeywords]
    ) -> None: ...
    def clearText(self) -> None: ...
    def setText(self, text: str | Sequence[str] | None = None) -> None: ...
    def clearGeom(self) -> None: ...
    def setGeom(self, geom: MaybeGeomOrSequence = None) -> None: ...
    def clearImage(self) -> None: ...
    def setImage(self, image: MaybeImageOrSequence = None) -> None: ...
