from __future__ import annotations
from enum import Enum
from typing import Final

from PySide6.QtWidgets import QDockWidget, QWidget
from PySide6.QtGui import Qt


class _DockWidgetFeatures:
    NO_DOCK_WIDGET_FEATURES: Final[int] = 0X00
    DOCK_WIDGET_CLOSABLE: Final[int] = 0X01
    DOCK_WIDGET_MOVABLE: Final[int] = 0X02
    DOCK_WIDGET_FLOATABLE: Final[int] = 0X04
    DOCK_WIDGET_VERTICAL_TITLE_BAR: Final[int] = 0X08


class _DockWidgetAreas:
    NO_DOCK_WIDGET_AREA: Final[int] = 0X00
    LEFT_DOCK_WIDGET_AREA: Final[int] = 0X01
    RIGHT_DOCK_WIDGET_AREA: Final[int] = 0X02
    TOP_DOCK_WIDGET_AREA: Final[int] = 0X04
    BOTTOM_DOCK_WIDGET_AREA: Final[int] = 0X08


class Dock:
    __slots__ = (
        '_dock',
        '_features',
        '_areas'
    )

    def __init__(self, parent: QWidget = None):
        self._dock: QDockWidget = QDockWidget(parent)
        self._features: list[int] = [
            _DockWidgetFeatures.DOCK_WIDGET_CLOSABLE,
            _DockWidgetFeatures.DOCK_WIDGET_MOVABLE,
            _DockWidgetFeatures.DOCK_WIDGET_FLOATABLE
        ]
        self._areas: list[int] = [
            _DockWidgetAreas.LEFT_DOCK_WIDGET_AREA,
            _DockWidgetAreas.RIGHT_DOCK_WIDGET_AREA,
            _DockWidgetAreas.TOP_DOCK_WIDGET_AREA,
            _DockWidgetAreas.BOTTOM_DOCK_WIDGET_AREA
        ]

    def set_feature_not_closable(self) -> Dock:
        self._features.remove(_DockWidgetFeatures.DOCK_WIDGET_CLOSABLE)
        return self

    def set_feature_not_movable(self) -> Dock:
        self._features.remove(_DockWidgetFeatures.DOCK_WIDGET_MOVABLE)
        return self

    def set_feature_not_floatable(self) -> Dock:
        self._features.remove(_DockWidgetFeatures.DOCK_WIDGET_FLOATABLE)
        return self

    def set_feature_vertical_title_bar(self) -> Dock:
        self._features.append(_DockWidgetFeatures.DOCK_WIDGET_VERTICAL_TITLE_BAR)
        return self

    def set_not_dockable_to_left(self) -> Dock:
        self._features.remove(_DockWidgetAreas.LEFT_DOCK_WIDGET_AREA)
        return self

    def set_not_dockable_to_right(self) -> Dock:
        self._features.remove(_DockWidgetAreas.RIGHT_DOCK_WIDGET_AREA)
        return self

    def set_not_dockable_to_top(self) -> Dock:
        self._features.remove(_DockWidgetAreas.TOP_DOCK_WIDGET_AREA)
        return self

    def set_not_dockable_to_bottom(self) -> Dock:
        self._features.remove(_DockWidgetAreas.BOTTOM_DOCK_WIDGET_AREA)
        return self

    def set_not_floating(self) -> Dock:
        self._dock.setFloating(False)
        return self

    def set_titlebar_widget(self, widget: QWidget) -> Dock:
        self._dock.setTitleBarWidget(widget)
        return self

    def set_dock_widget(self, widget: QWidget) -> Dock:
        self._dock.setWidget(widget)
        return self
