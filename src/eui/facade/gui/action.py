from __future__ import annotations
from typing import Any, Callable

from PySide6.QtGui import QIcon, QPixmap, QKeySequence, QActionGroup, QFont, QAction


class Action:
    """
    Generates a QAction instance.

    https://doc.qt.io/qtforpython/PySide6/QtGui/QAction.html#PySide6.QtGui.PySide6.QtGui.QAction.triggered
    """
    __slots__ = ('_action',)

    def __init__(self, parent=None):
        self._action: QAction = QAction(parent=parent)

    @property
    def get(self) -> QAction:
        return self._action

    def on_changed(self, callback: Callable[[], None]) -> Action:
        self._action.changed.connect(callback)
        return self

    def on_checkable_changed(self, callback: Callable[[bool], None]) -> Action:
        """
        Connects "checkableChanged"
        :param callback: ``def on_checkable_changed(self, is_checkable: bool)``
        """
        self._action.checkableChanged.connect(callback)
        return self

    def on_enabled_changed(self, callback: Callable[[bool], None]) -> Action:
        """
        Connects "enabledChanged"
        :param callback: ``def on_enabled_changed(self, is_enabled: bool)``
        """
        self._action.enabledChanged.connect(callback)
        return self

    def on_hovered(self, callback: Callable[[], None]) -> Action:
        self._action.hovered.connect(callback)
        return self

    def on_toggled(self, callback: Callable[[bool], None]) -> Action:
        """
        Connects "toggled"
        :param callback: ``def on_toggled(self, is_toggled: bool)``
        """
        self._action.toggled.connect(callback)
        return self

    def on_triggered(self, callback: Callable[[], None]) -> Action:
        self._action.triggered.connect(callback)
        return self

    def on_visible_changed(self, callback: Callable[[], None]) -> Action:
        self._action.visibleChanged.connect(callback)
        return self

    def set_text(self, text: str) -> Action:
        """
        This property holds the action’s descriptive text. If the action is added to a menu, the menu option will consist of the icon (if there is one), the text, and the shortcut (if there is one). If the text is not explicitly set in the constructor, or by using setText(), the action’s description icon text will be used as text. There is no default text.
        """
        self._action.setText(text)
        return self

    def set_action_group(self, action_group: QActionGroup) -> Action:
        """
        Sets this action group to group. The action will be automatically added to the group’s list of actions. Actions within the group will be mutually exclusive.
        """
        self._action.setActionGroup(action_group)
        return self

    def set_no_auto_repeats(self) -> Action:
        """
        This property holds whether the action can auto repeat. If true, the action will auto repeat when the keyboard shortcut combination is held down, provided that keyboard auto repeat is enabled on the system. The default value is true.
        """
        self._action.setAutoRepeat(False)
        return self

    def set_checkable(self) -> Action:
        """
        This property holds whether the action is a checkable action. A checkable action is one which has an on/off state. For example, in a word processor, a Bold toolbar button may be either on or off. An action which is not a toggle action is a command action; a command action is simply executed, e.g. file save. By default, this property is false.
        """
        self._action.setCheckable(True)
        return self

    def set_data(self, data: Any) -> Action:
        """
        Sets the action’s internal data to the given data.
        """
        self._action.setData(data)
        return self

    def set_disable(self) -> Action:
        """
        This property holds whether the action is enabled. Disabled actions cannot be chosen by the user. They do not disappear from menus or toolbars, but they are displayed in a way which indicates that they are unavailable. For example, they might be displayed using only shades of gray.
        """
        self._action.setDisabled(True)
        return self

    def set_font(self, font: QFont) -> Action:
        """
        This property holds the action’s font. The font property is used to render the text set on the QAction . The font can be considered a hint as it will not be consulted in all cases based upon application and style. By default, this property contains the application’s default font.
        """
        self._action.setFont(font)
        return self

    def set_icon(self, icon: QIcon | QPixmap | None) -> Action:
        """
        This property holds the action’s icon. In toolbars, the icon is used as the tool button icon; in menus, it is displayed to the left of the menu text. There is no default icon.
        """
        self._action.setIcon(icon)
        return self

    def set_icon_text(self, icon_text: str) -> Action:
        """
        This property holds the action’s descriptive icon text. If toolButtonStyle is set to a value that permits text to be displayed, the text defined held in this property appears as a label in the relevant tool button.
        """
        self._action.setIconText(icon_text)
        return self

    def set_icon_visible(self, visible: bool) -> Action:
        """
        This property holds whether or not an action should show an icon in a menu.
        """
        self._action.setIconVisibleInMenu(visible)
        return self

    def set_priority(self, priority: EventPriorities) -> Action:
        """
        This property holds the actions’s priority in the user interface. This property can be set to indicate how the action should be prioritized in the user interface. For instance, when toolbars have the ToolButtonTextBesideIcon mode set, then actions with LowPriority will not show the text labels.
        """
        self._action.setPriority(priority)
        return self

    def set_shortcut(self, shortcut: str) -> Action:
        """
        This property holds the action’s primary shortcut key. Valid keycodes for this property can be found in Key and Modifier . There is no default shortcut key.
        """
        self._action.setShortcut(QKeySequence(shortcut))
        return self

    def set_shortcut_context(self, shortcut_context: ShortcutContexts) -> Action:
        """
        This property holds the context for the action’s shortcut. Valid values for this property can be found in ShortcutContext . The default value is WindowShortcut .
        """
        self._action.setShortcutContext(shortcut_context)
        return self

    def set_status_bar_tip(self, status_bar_tip: str) -> Action:
        """
        This property holds the action’s status tip. The status tip is displayed on all status bars provided by the action’s top-level parent widget.
        """
        self._action.setStatusTip(status_bar_tip)
        return self

    def set_tooltip(self, tooltip: str) -> Action:
        """
        This property holds the action’s tooltip. This text is used for the tooltip. If no tooltip is specified, the action’s text is used.
        """
        self._action.setToolTip(tooltip)
        return self

    def set_visible(self, visible: bool) -> Action:
        """
        This property holds whether the action can be seen (e.g. in menus and toolbars).
        """
        self._action.setVisible(visible)
        return self

    def set_whats_this(self, whats_this: str) -> Action:
        """
        This property holds the action’s “What’s This?” help text. The “What’s This?” text is used to provide a brief description of the action. The text may contain rich text. There is no default “What’s This?” text.
        """
        self._action.setWhatsThis(whats_this)
        return self