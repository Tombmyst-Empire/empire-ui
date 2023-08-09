from __future__ import annotations

from typing import Callable, Any

from PySide6.QtCore import QObject, QEvent, QTimerEvent
from PySide6.QtGui import (
    QPaintEvent,
    QCloseEvent,
    QFocusEvent,
    QEnterEvent,
    QKeyEvent,
    QMouseEvent,
    QMoveEvent,
    QResizeEvent,
    QAction,
    QDragLeaveEvent, QDragMoveEvent, QDropEvent, QDragEnterEvent
)
from PySide6.QtWidgets import QWidget

from eui.facade.gui.action import Action


class Widget:
    __slots__ = (
        '_built_widget',
        '_paint_event_listeners',
        '_close_event_listeners',
        '_focus_event_listeners',
        '_unfocus_event_listeners',
        '_mouse_enter_event_listeners',
        '_mouse_leave_event_listeners',
        '_key_press_event_listeners',
        '_key_release_event_listeners',
        '_mouse_double_click_event_listeners',
        '_mouse_move_event_listeners',
        '_mouse_press_event_listeners',
        '_mouse_release_event_listeners',
        '_move_event_listeners',
        '_resize_event_listeners',
        '_timer_event_listeners',
        '_drag_enter_event_listeners',
        '_drag_leave_event_listeners',
        '_drag_move_event_listeners',
        '_drag_drop_event_listeners'
    )

    def __init__(
        self,
        *,
        qparent: QWidget = None,
        parent: Widget = None,
        built_widget_instance: QWidget = None
    ):
        self._built_widget: QWidget = (
            built_widget_instance if built_widget_instance is not None else QWidget()
        )
        self._built_widget.setParent(qparent or parent)

        self._close_event_listeners: list[Callable[[QCloseEvent], None]] = []
        self._move_event_listeners: list[Callable[[QMoveEvent], None]] = []
        self._resize_event_listeners: list[Callable[[QResizeEvent], None]] = []
        self._paint_event_listeners: list[Callable[[QPaintEvent], None]] = []
        self._timer_event_listeners: list[Callable[[QTimerEvent], None]] = []

        self._focus_event_listeners: list[Callable[[QFocusEvent], None]] = []
        self._unfocus_event_listeners: list[Callable[[QFocusEvent], None]] = []

        self._mouse_enter_event_listeners: list[Callable[[QEnterEvent], None]] = []
        self._mouse_leave_event_listeners: list[Callable[[QEvent], None]] = []
        self._mouse_double_click_event_listeners: list[Callable[[QMouseEvent], None]] = []
        self._mouse_move_event_listeners: list[Callable[[QMouseEvent], None]] = []
        self._mouse_press_event_listeners: list[Callable[[QMouseEvent], None]] = []
        self._mouse_release_event_listeners: list[Callable[[QMouseEvent], None]] = []

        self._key_press_event_listeners: list[Callable[[QKeyEvent], None]] = []
        self._key_release_event_listeners: list[Callable[[QKeyEvent], None]] = []

        self._drag_enter_event_listeners: list[Callable[[QDragEnterEvent], None]] = []
        self._drag_leave_event_listeners: list[Callable[[QDragLeaveEvent], None]] = []
        self._drag_move_event_listeners: list[Callable[[QDragMoveEvent], None]] = []
        self._drag_drop_event_listeners: list[Callable[[QDropEvent], None]] = []

        self._built_widget.paintEvent = self._paint_event
        self._built_widget.closeEvent = self._close_event
        self._built_widget.focusInEvent = self._focus_event
        self._built_widget.focusOutEvent = self._unfocus_event
        self._built_widget.enterEvent = self._mouse_enter_event
        self._built_widget.keyPressEvent = self._key_press_event
        self._built_widget.keyReleaseEvent = self._key_release_event
        self._built_widget.leaveEvent = self._mouse_leave_event
        self._built_widget.mouseDoubleClickEvent = self._mouse_double_click_event
        self._built_widget.mouseMoveEvent = self._mouse_move_event
        self._built_widget.mousePressEvent = self._mouse_press_event
        self._built_widget.mouseReleaseEvent = self._mouse_release_event
        self._built_widget.moveEvent = self._move_event
        self._built_widget.resizeEvent = self._resize_event
        self._built_widget.timerEvent = self._timer_event

    def on_destroy(self, callback: Callable[[Any], None]) -> Widget:
        """
        This signal is emitted immediately before the object obj is destroyed, after any instances
        of QPointer have been notified, and cannot be blocked.

        All the objects’s children are destroyed immediately after this signal is emitted.
        :param callback: ``def on_destroy(self, object_to_destroy: Any)``
        :return:
        """
        self._built_widget.destroy.connect(callback)
        return self

    def on_object_name_changed(self, callback: Callable[[str], None]) -> Widget:
        """
        This signal is emitted after the object’s name has been changed. The new object name is passed as objectName.
        :param callback: ``def on_object_name_changed(self, new_object_name: str)``
        """
        self._built_widget.objectNameChanged.connect(callback)
        return self

    def on_paint(self, callback: Callable[[QPaintEvent], None]) -> Widget:
        """
        Registers *callback* as a listener for the QT *paint event*

        See: https://doc.qt.io/qt-6/qwidget.html#paintEvent
        """
        self._paint_event_listeners.append(callback)
        return self

    def on_close(self, callback: Callable[[QCloseEvent], None]) -> Widget:
        """
        Registers *callback* as a listener for the QT *close event*

        See: https://doc.qt.io/qt-6/qwidget.html#closeEvent
        """
        self._close_event_listeners.append(callback)
        return self

    def on_focus(self, callback: Callable[[QFocusEvent], None]) -> Widget:
        """
        Registers *callback* as a listener for the QT *focus-in event*

        See: https://doc.qt.io/qt-6/qwidget.html#focusInEvent
        """
        self._focus_event_listeners.append(callback)
        return self

    def on_unfocus(self, callback: Callable[[QFocusEvent], None]) -> Widget:
        """
        Registers *callback* as a listener for the QT *focus-out event*

        See: https://doc.qt.io/qt-6/qwidget.html#focusOutEvent
        """
        self._unfocus_event_listeners.append(callback)
        return self

    def on_mouse_enter(self, callback: Callable[[QEnterEvent], None]) -> Widget:
        """
        Registers *callback* as a listener for the QT *enter event*

        See: https://doc.qt.io/qt-6/qwidget.html#enterEvent
        """
        self._mouse_enter_event_listeners.append(callback)
        return self

    def on_key_press(self, callback: Callable[[QKeyEvent], None]) -> Widget:
        """
        Registers *callback* as a listener for the QT *key press*

        See: https://doc.qt.io/qt-6/qwidget.html#keyPressEvent
        """
        self._key_press_event_listeners.append(callback)
        return self

    def on_key_release(self, callback: Callable[[QKeyEvent], None]) -> Widget:
        """
        Registers *callback* as a listener for the QT *key release*

        See: https://doc.qt.io/qt-6/qwidget.html#keyReleaseEvent
        """
        self._key_release_event_listeners.append(callback)
        return self

    def on_mouse_leave(self, callback: Callable[[QEvent], None]) -> Widget:
        """
        Registers *callback* as a listener for the QT *leave*

        See: https://doc.qt.io/qt-6/qwidget.html#leaveEvent
        """
        self._mouse_leave_event_listeners.append(callback)
        return self

    def on_mouse_double_click(self, callback: Callable[[QMouseEvent], None]) -> Widget:
        """
        Registers *callback* as a listener for the QT *mouse double click*

        See: https://doc.qt.io/qt-6/qwidget.html#mouseDoubleClickEvent
        """
        self._mouse_double_click_event_listeners.append(callback)
        return self

    def on_mouse_move(self, callback: Callable[[QMouseEvent], None]) -> Widget:
        """
        Registers *callback* as a listener for the QT *mouse move*

        See: https://doc.qt.io/qt-6/qwidget.html#mouseMoveEvent
        """
        self._mouse_move_event_listeners.append(callback)
        return self

    def on_mouse_press(self, callback: Callable[[QMouseEvent], None]) -> Widget:
        """
        Registers *callback* as a listener for the QT *mouse click*

        See: https://doc.qt.io/qt-6/qwidget.html#mousePressEvent
        """
        self._mouse_press_event_listeners.append(callback)
        return self

    def on_mouse_release(self, callback: Callable[[QMouseEvent], None]) -> Widget:
        """
        Registers *callback* as a listener for the QT *mouse click*

        See: https://doc.qt.io/qt-6/qwidget.html#mouseReleaseEvent
        """
        self._mouse_release_event_listeners.append(callback)
        return self

    def on_move(self, callback: Callable[[QMoveEvent], None]) -> Widget:
        """
        Registers *callback* as a listener for the QT *move*

        See: https://doc.qt.io/qt-6/qwidget.html#moveEvent
        """
        self._move_event_listeners.append(callback)
        return self

    def on_resize(self, callback: Callable[[QResizeEvent], None]) -> Widget:
        """
        Registers *callback* as a listener for the QT *resize*

        See: https://doc.qt.io/qt-6/qwidget.html#resizeEvent
        """
        self._resize_event_listeners.append(callback)
        return self

    def on_timer(self, callback: Callable[[QTimerEvent], None]) -> Widget:
        """
        Registers *callback* as a listener for the QT *timer*

        See: https://doc.qt.io/qt-6/qobject.html#timerEvent
        """
        self._timer_event_listeners.append(callback)
        return self

    def on_drag_enter(self, callback: Callable[[QDragEnterEvent], None]) -> Widget:
        """
        Registers *callback* as a listener for the QT *drag enter*

        See: https://doc.qt.io/qtforpython/PySide6/QtWidgets/QWidget.html#PySide6.QtWidgets.PySide6.QtWidgets.QWidget.dragEnterEvent
        """
        self._drag_enter_event_listeners.append(callback)
        return self

    def on_drag_leave(self, callback: Callable[[QDragLeaveEvent], None]) -> Widget:
        """
        Registers *callback* as a listener for the QT *drag leave*

        See: https://doc.qt.io/qtforpython/PySide6/QtWidgets/QWidget.html#PySide6.QtWidgets.PySide6.QtWidgets.QWidget.dragLeaveEvent
        """
        self._drag_leave_event_listeners.append(callback)
        return self

    def on_drag_move(self, callback: Callable[[QDragMoveEvent], None]) -> Widget:
        """
        Registers *callback* as a listener for the QT *drag move*

        See: https://doc.qt.io/qtforpython/PySide6/QtWidgets/QWidget.html#PySide6.QtWidgets.PySide6.QtWidgets.QWidget.dragMoveEvent
        """
        self._drag_move_event_listeners.append(callback)
        return self

    def on_drag_drop(self, callback: Callable[[QDropEvent], None]) -> Widget:
        """
        Registers *callback* as a listener for the QT *drop*

        See: https://doc.qt.io/qtforpython/PySide6/QtWidgets/QWidget.html#PySide6.QtWidgets.PySide6.QtWidgets.QWidget.dropEvent
        """
        self._drag_drop_event_listeners.append(callback)
        return self

    def add_action(self, action: Action) -> Widget:
        self._built_widget.addAction(action.get)
        return self

    def add_qaction(self, action: QAction) -> Widget:
        self._built_widget.addAction(action)
        return self

    def _paint_event(self, event: QPaintEvent):
        QWidget.paintEvent(self, event)
        [callback(event) for callback in self._paint_event_listeners]

    def _close_event(self, event: QCloseEvent):
        QWidget.closeEvent(self, event)
        [callback(event) for callback in self._close_event_listeners]

    def _focus_event(self, event: QFocusEvent):
        QWidget.focusInEvent(self, event)
        [callback(event) for callback in self._focus_event_listeners]

    def _unfocus_event(self, event: QFocusEvent):
        QWidget.focusOutEvent(self, event)
        [callback(event) for callback in self._unfocus_event_listeners]

    def _mouse_enter_event(self, event: QEnterEvent):
        QWidget.enterEvent(self, event)
        [callback(event) for callback in self._mouse_enter_event_listeners]

    def _key_press_event(self, event: QKeyEvent):
        QWidget.keyPressEvent(self, event)
        [callback(event) for callback in self._key_press_event_listeners]

    def _key_release_event(self, event: QKeyEvent):
        QWidget.keyReleaseEvent(self, event)
        [callback(event) for callback in self._key_release_event_listeners]

    def _mouse_leave_event(self, event: QEvent):
        QWidget.leaveEvent(self, event)
        [callback(event) for callback in self._mouse_leave_event_listeners]

    def _mouse_double_click_event(self, event: QMouseEvent):
        QWidget.mouseDoubleClickEvent(self, event)
        [callback(event) for callback in self._mouse_double_click_event_listeners]

    def _mouse_move_event(self, event: QMouseEvent):
        QWidget.mouseMoveEvent(self, event)
        [callback(event) for callback in self._mouse_move_event_listeners]

    def _mouse_press_event(self, event: QMouseEvent):
        QWidget.mousePressEvent(self, event)
        [callback(event) for callback in self._mouse_press_event_listeners]

    def _mouse_release_event(self, event: QMouseEvent):
        QWidget.mouseReleaseEvent(self, event)
        [callback(event) for callback in self._mouse_release_event_listeners]

    def _move_event(self, event: QMoveEvent):
        QWidget.moveEvent(self, event)
        [callback(event) for callback in self._move_event_listeners]

    def _resize_event(self, event: QResizeEvent):
        QWidget.resizeEvent(self, event)
        [callback(event) for callback in self._resize_event_listeners]

    def _timer_event(self, event: QTimerEvent):
        QWidget.timerEvent(self, event)
        [callback(event) for callback in self._timer_event_listeners]
