from __future__ import annotations
from PySide6.QtCore import QObject, QChildEvent


class Object:
    __slots__ = (
        '_built_object'
    )

    def __init__(
        self,
        built_object: QObject = None,
        parent: QObject = None
    ):
        self._built_object: QObject = built_object or QObject(parent)

    @property
    def object_name(self) -> str:
        """
        This property holds the name of this object.
        You can find an object by name (and type) using findChild() . You can find a set of objects with findChildren() .
        """
        return self._built_object.objectName()

    @object_name.setter
    def object_name(self, name: str):
        self._built_object.setObjectName(name)

    def block_signals(self, state: bool) -> Object:
        """
        If block is true, signals emitted by this object are blocked (i.e., emitting a signal will not invoke anything connected to it). If block is false, no such blocking will occur.

        The return value is the previous value of signalsBlocked() .

        Note that the destroyed() signal will be emitted even if the signals for this object have been blocked.

        Signals emitted while being blocked are not buffered.
        """
        self._built_object.blockSignals(state)
        return self

    def child_event(self, event: QChildEvent) -> Object:
        """
        This event handler can be reimplemented in a subclass to receive child events. The event is passed in the event parameter.

        ChildAdded and ChildRemoved events are sent to objects when children are added or removed. In both cases you can only rely on the child being a QObject , or if isWidgetType() returns true, a QWidget . (This is because, in the ChildAdded case, the child is not yet fully constructed, and in the ChildRemoved case it might have been destructed already).

        ChildPolished events are sent to widgets when children are polished, or when polished children are added. If you receive a child polished event, the child’s construction is usually completed. However, this is not guaranteed, and multiple polish events may be delivered during the execution of a widget’s constructor.

        For every child widget, you receive one ChildAdded event, zero or more ChildPolished events, and one ChildRemoved event.

        The ChildPolished event is omitted if a child is removed immediately after it is added. If a child is polished several times during construction and destruction, you may receive several child polished events for the same child, each time with a different virtual table.
        """
