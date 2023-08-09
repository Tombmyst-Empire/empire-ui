from enum import Enum, auto
from typing import Any, Optional

from empire_commons.entry_point.main_base import Main, AsyncMain
import ereport


LOGGER = ereport.get_or_make_reporter('EUI', 'E_UI_LOGGING_LEVEL')


class ApplicationType(Enum):
    DEFAULT = auto()  #: QApplication: QApplication specializes QGuiApplication with some functionality needed for QWidget-based applications. It handles widget specific initialization, finalization.
    NON_GUI = auto()  #: This class is used by non-GUI applications to provide their event loop. For non-GUI application that uses Qt, there should be exactly one QCoreApplication object.
    GUI = auto()  #: QGuiApplication contains the main event loop, where all events from the window system and other sources are processed and dispatched. It also handles the application's initialization and finalization, and provides session management. In addition, QGuiApplication handles most of the system-wide and application-wide settings.



class QtMain(Main):
    __slots__ = (
        'app',
        'application_type',
        'exited_with_success',
        'qt_exit_code'
    )

    def __init__(
        self,
        program_name: str,
        program_version: str,
        program_headline: str,
        application_type: ApplicationType = ApplicationType.DEFAULT,
        *,
        receives_args: bool = False
    ):
        if ApplicationType.DEFAULT:
            from PySide6.QtWidgets import QApplication as Application
        elif ApplicationType.NON_GUI:
            from PySide6.QtCore import QCoreApplication as Application
        elif ApplicationType.GUI:
            from PySide6.QtGui import QGuiApplication as Application
        else:
            raise ValueError(f'Unknown value: {application_type}')

        super().__init__(
            program_name,
            program_version,
            program_headline,
            receives_args=receives_args
        )

        self.app = None
        self.application_type: type = Application
        self.exited_with_success: Optional[bool] = None
        self.qt_exit_code: int = 0

    def init(self, parsed_args: dict[str, Any], *args, **kwargs):
        if not super().init(parsed_args, *args, **kwargs):
            return False

        args_as_list: list[str] = []
        for arg_name, arg_val in parsed_args:
            args_as_list.extend([arg_name, arg_val])

        self.app = self.application_type(args_as_list)
        return True

    def main(self, parsed_args: dict[str, Any], *args, **kwargs) -> bool:
        if not super().main(parsed_args, *args, **kwargs):
            return False

        self.qt_exit_code: int = self.app.exec()
        if self.qt_exit_code == 0:
            self.exited_with_success = True
            LOGGER.success('Exiting QT app with code 0')
        else:
            self.exited_with_success = False
            LOGGER.warn(f'Exiting QT app with code {self.qt_exit_code}')

        return True


class AsyncQtMain(AsyncMain):
    __slots__ = (
        'app',
        'application_type',
        'exited_with_success',
        'qt_exit_code'
    )

    def __init__(
        self,
        program_name: str,
        program_version: str,
        program_headline: str,
        application_type: ApplicationType = ApplicationType.DEFAULT,
        *,
        receives_args: bool = False
    ):
        if ApplicationType.DEFAULT:
            from PySide6.QtWidgets import QApplication as Application
        elif ApplicationType.NON_GUI:
            from PySide6.QtCore import QCoreApplication as Application
        elif ApplicationType.GUI:
            from PySide6.QtGui import QGuiApplication as Application
        else:
            raise ValueError(f'Unknown value: {application_type}')

        super().__init__(
            program_name,
            program_version,
            program_headline,
            receives_args=receives_args
        )

        self.app = None
        self.application_type: type = Application
        self.exited_with_success: Optional[bool] = None
        self.qt_exit_code: int = 0

    async def init(self, parsed_args: dict[str, Any], *args, **kwargs):
        if not await super().init(parsed_args, *args, **kwargs):
            return False

        args_as_list: list[str] = []
        for arg_name, arg_val in parsed_args:
            args_as_list.extend([arg_name, arg_val])

        self.app = self.application_type(args_as_list)
        return True

    async def main(self, parsed_args: dict[str, Any], *args, **kwargs) -> bool:
        if not await super().main(parsed_args, *args, **kwargs):
            return False

        self.qt_exit_code: int = self.app.exec()
        if self.qt_exit_code == 0:
            self.exited_with_success = True
            LOGGER.success('Exiting QT app with code 0')
        else:
            self.exited_with_success = False
            LOGGER.warn(f'Exiting QT app with code {self.qt_exit_code}')

        return True
