from _typeshed import Unused
from typing import Any, ClassVar, Literal
from typing_extensions import TypeAlias

from direct.directnotify.Notifier import Notifier
from direct.showbase.DirectObject import DirectObject
from panda3d._typing import Vec3Like
from panda3d.core import (
    Camera,
    Connection,
    ConnectionWriter,
    DatagramIterator,
    Lens,
    LVector3f,
    NodePath,
    QueuedConnectionListener,
    QueuedConnectionManager,
    QueuedConnectionReader,
)

from .ClusterMsgs import ClusterMsgHandler

_NamedMovement: TypeAlias = tuple[
    str, float, float, float, float, float, float, float, float, float, float, float, float, float, bool
]
_TaskCont: TypeAlias = Literal[1]

class ClusterServer(DirectObject):
    notify: ClassVar[Notifier]
    MSG_NUM: ClassVar[int]
    cameraJig: NodePath
    camera: NodePath[Camera]
    lens: Lens
    lastConnection: Connection | None
    fPosReceived: bool
    qcm: QueuedConnectionManager
    qcl: QueuedConnectionListener
    qcr: QueuedConnectionReader
    cw: ConnectionWriter
    tcpRendezvous: Connection
    msgHandler: ClusterMsgHandler
    daemon: Any
    objectMappings: dict[str, NodePath]
    objectHasColor: dict[str, bool]
    controlMappings: dict[str, str]
    controlPriorities: dict[str, int]
    controlOffsets: dict[str, LVector3f]
    messageQueue: list[_NamedMovement]
    sortedControlMappings: list[tuple[int, str]]
    def __init__(self, cameraJig: NodePath, camera: NodePath[Camera]) -> None: ...
    def startListenerPollTask(self) -> None: ...
    def listenerPollTask(self, task: Unused) -> _TaskCont: ...
    def addNamedObjectMapping(self, object: NodePath, name: str, hasColor: bool = True, priority: Unused = 0) -> None: ...
    def removeObjectMapping(self, name: str) -> None: ...
    def redoSortedPriorities(self) -> None: ...
    def addControlMapping(
        self, objectName: str, controlledName: str, offset: LVector3f | None = None, priority: int = 0
    ) -> None: ...
    def setControlMappingOffset(self, objectName: str, offset: LVector3f) -> None: ...
    def removeControlMapping(self, name: str) -> None: ...
    def startControlObjectTask(self) -> None: ...
    def controlObjectTask(self, task: Unused) -> _TaskCont: ...
    def sendNamedMovementDone(self) -> None: ...
    def moveObject(self, nodePath: NodePath, object: str, offset: Vec3Like, hasColor: bool) -> None: ...
    def startReaderPollTask(self) -> None: ...
    def startSwapCoordinator(self) -> None: ...
    def swapCoordinatorTask(self, task: Unused) -> _TaskCont: ...
    def sendSwapReady(self) -> None: ...
    def handleDatagram(self, dgi: DatagramIterator, type: int) -> int: ...
    def handleCamOffset(self, dgi: DatagramIterator) -> None: ...
    def handleCamFrustum(self, dgi: DatagramIterator) -> None: ...
    def handleNamedMovement(self, data: _NamedMovement) -> None: ...
    def handleMessageQueue(self) -> None: ...
    def handleCamMovement(self, dgi: DatagramIterator) -> None: ...
    def handleSelectedMovement(self, dgi: DatagramIterator) -> None: ...
    def handleTimeData(self, dgi: DatagramIterator) -> None: ...
    def handleCommandString(self, dgi: DatagramIterator) -> None: ...
