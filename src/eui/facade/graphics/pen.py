from __future__ import annotations

from enum import Enum
from typing import Sequence

from PySide6.QtGui import QPen, QBrush, QColor
from PySide6.QtGui import Qt


class PenStyles(Enum):
    """
    This enum type defines the pen styles that can be drawn using QPainter

    https://doc.qt.io/qtforpython/PySide6/QtCore/Qt.html#PySide6.QtCore.PySide6.QtCore.Qt.PenStyle
    """
    NO_PEN = Qt.PenStyle.NoPen
    SOLID_LINE = Qt.PenStyle.SolidLine
    DASH_LINE = Qt.PenStyle.DashLine
    DOT_LINE = Qt.PenStyle.DotLine
    DASH_DOT_LINE = Qt.PenStyle.DashDotLine
    DASH_DOT_DOT_LINE = Qt.PenStyle.DashDotDotLine
    CUSTOM_DASH_LINE = Qt.PenStyle.CustomDashLine


class PenJoinStyles(Enum):
    """
    This enum type defines the pen join styles supported by Qt, i.e. which joins between two connected lines can be drawn using QPainter .

    https://doc.qt.io/qtforpython/PySide6/QtCore/Qt.html#PySide6.QtCore.PySide6.QtCore.Qt.PenJoinStyle
    """
    MITER_JOIN = Qt.PenJoinStyle.MiterJoin
    BEVEL_JOIN = Qt.PenJoinStyle.BevelJoin
    ROUND_JOIN = Qt.PenJoinStyle.RoundJoin
    SVG_MITER_JOIN = Qt.PenJoinStyle.SvgMiterJoin


class PenCapStyles(Enum):
    """
    This enum type defines the pen cap styles supported by Qt, i.e. the line end caps that can be drawn using QPainter .

    https://doc.qt.io/qtforpython/PySide6/QtCore/Qt.html#PySide6.QtCore.PySide6.QtCore.Qt.PenCapStyle
    """
    SQUARE_CAP = Qt.PenCapStyle.SquareCap
    FLAT_CAP = Qt.PenCapStyle.FlatCap
    ROUND_CAP = Qt.PenCapStyle.RoundCap


class Pen:
    """
    Builds a QPen instance
    """
    def __init__(self):
        self._pen = QPen()

    def get(self) -> QPen:
        return self._pen

    def set_brush(self, brush: QBrush) -> Pen:
        """
        Sets the brush used to fill strokes generated with this pen to the given brush.

        https://doc.qt.io/qtforpython/PySide6/QtGui/QPen.html#PySide6.QtGui.PySide6.QtGui.QPen.setBrush
        """
        self._pen.setBrush(brush)
        return self

    def set_cap_style(self, cap_style: PenCapStyles) -> Pen:
        """
        Sets the pen’s cap style to the given style. The default value is SquareCap .

        https://doc.qt.io/qtforpython/PySide6/QtGui/QPen.html#PySide6.QtGui.PySide6.QtGui.QPen.setCapStyle
        """
        self._pen.setCapStyle(cap_style.value)
        return self

    def set_color(self, color: QColor) -> Pen:
        """
        Sets the color of this pen’s brush to the given color.

        https://doc.qt.io/qtforpython/PySide6/QtGui/QPen.html#PySide6.QtGui.PySide6.QtGui.QPen.setColor
        """
        self._pen.setColor(color)
        return self

    def set_cosmetic(self, cosmetic: bool) -> Pen:
        """
        Sets this pen to cosmetic or non-cosmetic, depending on the value of cosmetic.

        https://doc.qt.io/qtforpython/PySide6/QtGui/QPen.html#PySide6.QtGui.PySide6.QtGui.QPen.setCosmetic
        """
        self._pen.setCosmetic(cosmetic)
        return self

    def set_dash_offset(self, offset: float) -> Pen:
        """
        Sets the dash offset (the starting point on the dash pattern) for this pen to the offset specified. The offset is measured in terms of the units used to specify the dash pattern.

        https://doc.qt.io/qtforpython/PySide6/QtGui/QPen.html#PySide6.QtGui.PySide6.QtGui.QPen.setDashOffset
        """
        self._pen.setDashOffset(offset)
        return self

    def set_dash_pattern(self, pattern: Sequence[float]) -> Pen:
        """
        Sets the dash pattern for this pen to the given pattern. This implicitly converts the style of the pen to CustomDashLine .

        The pattern must be specified as an even number of positive entries where the entries 1, 3, 5… are the dashes and 2, 4, 6… are the spaces. For example:

        https://doc.qt.io/qtforpython/PySide6/QtGui/QPen.html#PySide6.QtGui.PySide6.QtGui.QPen.setDashPattern
        """
        self._pen.setDashPattern(pattern)
        return self

    def set_join_style(self, style: PenJoinStyles) -> Pen:
        """
        Sets the pen’s join style to the given style. The default value is BevelJoin .

        Sets the pen’s join style to the given style. The default value is BevelJoin .
        """
        self._pen.setJoinStyle(style.value)
        return self

    def set_miter_limit(self, limit: float) -> Pen:
        """
        Sets the miter limit of this pen to the given limit.

        The miter limit describes how far a miter join can extend from the join point. This is used to reduce artifacts between line joins where the lines are close to parallel.

        https://doc.qt.io/qtforpython/PySide6/QtGui/QPen.html#PySide6.QtGui.PySide6.QtGui.QPen.setMiterLimit
        """
        self._pen.setMiterLimit(limit)
        return self

    def set_style(self, style: PenStyles) -> Pen:
        """
        Sets the pen style to the given style.

        https://doc.qt.io/qtforpython/PySide6/QtGui/QPen.html#PySide6.QtGui.PySide6.QtGui.QPen.setStyle
        """
        self._pen.setStyle(style.value)
        return self

    def set_width_i(self, width: int) -> Pen:
        """
        Sets the pen width to the given width in pixels with integer precision.

        https://doc.qt.io/qtforpython/PySide6/QtGui/QPen.html#PySide6.QtGui.PySide6.QtGui.QPen.setWidth
        """
        self._pen.setWidth(width)
        return self

    def set_width_f(self, width: float) -> Pen:
        """
        Sets the pen width to the given width in pixels with floating point precision.

        https://doc.qt.io/qtforpython/PySide6/QtGui/QPen.html#PySide6.QtGui.PySide6.QtGui.QPen.setWidthF
        """
        self._pen.setWidthF(width)
        return self
