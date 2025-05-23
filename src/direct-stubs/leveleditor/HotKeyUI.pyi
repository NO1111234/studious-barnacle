from _typeshed import Unused
from typing import Any

import wx  # type: ignore
import wx.siplib as sip  # type: ignore
from wx.lib.scrolledpanel import ScrolledPanel  # type: ignore

class EditHotKeyDialog(wx.Dialog, metaclass=sip.wrapper):
    currKey: str
    panel: wx.Panel
    label: wx.StaticText
    modifierRadio: wx.RadioBox
    specialKeyCombo: wx.Choice
    keyEntry: wx.TextCtrl
    def __init__(self, parent: Any, id, title, key: str) -> None: ...
    def updateUI(self) -> None: ...
    def onChangeModifier(self, evt) -> None: ...
    def onChangeSpecialKey(self, evt) -> None: ...
    def onApply(self, evt: Unused) -> None: ...

class HotKeyPanel(ScrolledPanel, metaclass=sip.wrapper):
    parent: Any
    def __init__(self, parent: Any) -> None: ...
    def updateUI(self) -> None: ...
    def onEdit(self, evt: Unused, key: str) -> None: ...

class HotKeyUI(wx.Dialog, metaclass=sip.wrapper):
    parent: Any
    def __init__(self, parent: Any, id, title) -> None: ...
