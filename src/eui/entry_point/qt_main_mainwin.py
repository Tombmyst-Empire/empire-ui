from typing import Any, Optional, Type, TypeVar, Generic

from PySide6.QtWidgets import QMainWindow

from eui.entry_point.qt_main import QtMain, ApplicationType, AsyncQtMain
from empire_commons.exceptions import ProgrammingException
import ereport


T = TypeVar('T', bound=QMainWindow)
LOGGER = ereport.get_or_make_reporter('EUI', 'E_UI_LOGGING_LEVEL')


class QtMainMainwin(Generic[T], QtMain):
    __slots__ = (
        'mainwin',
        'mainwin_class'
    )

    def __init__(
        self,
        program_name: str,
        program_version: str,
        program_headline: str,
        mainwin_impl: Type[T],
        *,
        receives_args: bool = False
    ):
        super().__init__(
            program_name,
            program_version,
            program_headline,
            application_type=ApplicationType.DEFAULT,
            receives_args=receives_args
        )

        self.mainwin_class: Type[T] = mainwin_impl
        self.mainwin: Optional[T] = None

    def postinit(self, parsed_args: dict[str, Any], *args, **kwargs) -> bool:
        if not super().postinit(parsed_args, *args, **kwargs):
            return False

        self.mainwin = self.mainwin_class()
        try:
            self.mainwin.show()
        except AttributeError:
            LOGGER.error('No attribute "show" was found in the MainWin implementation class. For reminder, '
                         'this class should inherit from "QMainWindow", have a dunder init method and this '
                         'method first 3 lines should be:\n\tsuper().__init__()\n\tself.ui = <INSERT MAIN WIN IMPL CLASS>()\n\t'
                         'self.ui.setupUi(self)')
            raise ProgrammingException('Poorly written MainWin implementation class.')

        return True


class AsyncQtMainMainwin(Generic[T], AsyncQtMain):
    __slots__ = (
        'mainwin',
        'mainwin_class'
    )

    def __init__(
        self,
        program_name: str,
        program_version: str,
        program_headline: str,
        mainwin_impl: Type[T],
        *,
        receives_args: bool = False
    ):
        super().__init__(
            program_name,
            program_version,
            program_headline,
            application_type=ApplicationType.DEFAULT,
            receives_args=receives_args
        )

        self.mainwin_class: Type[T] = mainwin_impl
        self.mainwin: Optional[T] = None

    async def postinit(self, parsed_args: dict[str, Any], *args, **kwargs) -> bool:
        if not await super().postinit(parsed_args, *args, **kwargs):
            return False

        self.mainwin = self.mainwin_class()
        self.mainwin.show()
        return True
