from _typeshed import Unused
from typing import Any, ClassVar, Literal

from panda3d.core import AsyncTask

from .CartesianGridBase import CartesianGridBase
from .ClientRepository import ClientRepository
from .DistributedNodeAI import DistributedNodeAI

class DistributedCartesianGridAI(DistributedNodeAI, CartesianGridBase):
    RuleSeparator: ClassVar[str]
    style: str
    startingZone: int
    gridSize: int
    gridRadius: float
    cellWidth: float
    gridObjects: dict[int, Any]
    updateTaskStarted: bool
    def __init__(
        self,
        air: ClientRepository,
        startingZone: int,
        gridSize: int,
        gridRadius: float,
        cellWidth: float,
        style: str = 'Cartesian',
    ) -> None: ...
    def getCellWidth(self) -> float: ...
    def getParentingRules(self) -> tuple[str, str]: ...
    def addObjectToGrid(self, av, useZoneId: int = -1, startAutoUpdate: bool = True) -> None: ...
    def removeObjectFromGrid(self, av) -> None: ...
    def startUpdateGridTask(self) -> None: ...
    def stopUpdateGridTask(self) -> None: ...
    def updateGridTask(self, task: AsyncTask | None = None) -> Literal[2]: ...
    def handleAvatarZoneChange(self, av, useZoneId: int = -1) -> None: ...
    def handleSetLocation(self, av: Unused, parentId: Unused, zoneId: Unused) -> None: ...
