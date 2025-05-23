__all__ = ['execfile', 'exists', 'getmtime', 'getsize', 'isdir', 'isfile', 'join', 'lexists', 'listdir', 'open', 'walk']

from _typeshed import ReadableBuffer, StrOrBytesPath, Unused
from collections.abc import Generator, Iterable, Mapping
from io import IOBase
from posixpath import join as join
from typing import Any

from panda3d.core import VirtualFile, istream, ostream

def open(
    file: StrOrBytesPath | VirtualFile | istream | ostream,
    mode: str = 'r',
    buffering: int = -1,
    encoding: str | None = None,
    errors: str | None = None,
    newline: str | None = None,
    closefd: bool = True,
) -> Any: ...

class StreamIOWrapper(IOBase):
    def __init__(self, stream: istream | ostream, needsVfsClose: bool = False) -> None: ...
    def read(self, size: int | None = -1) -> bytes: ...
    read1 = read
    def readline(self, size: Unused = -1) -> bytes: ...
    def seek(self, offset: int, whence: int = 0) -> None: ...  # type: ignore[override]
    def write(self, b: bytes) -> int: ...
    def writelines(self, lines: Iterable[ReadableBuffer]) -> None: ...

def listdir(path: str) -> list[str]: ...
def walk(
    top: StrOrBytesPath, topdown: bool = True, onerror: object = None, followlinks: bool = True
) -> Generator[tuple[StrOrBytesPath, list[str], list[str]], None, None]: ...
def isfile(path: str) -> bool: ...
def isdir(path: str) -> bool: ...
def exists(path: str) -> bool: ...
def lexists(path: str) -> bool: ...
def getmtime(path: str) -> int: ...
def getsize(path: str) -> int: ...
def execfile(path: str, globals: dict[str, Any] | None = None, locals: Mapping[str, object] | None = None) -> None: ...
