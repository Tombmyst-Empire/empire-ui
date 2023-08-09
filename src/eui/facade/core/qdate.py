from __future__ import annotations
from datetime import datetime

from PySide6.QtCore import QDate, QCalendar

from eui.facade.enums.date_enums import QTDayOfWeek, QTMonth


class Date:
    """
    https://doc.qt.io/qtforpython-6/PySide6/QtCore/QDate.html

    Missing:

    -  PySide6.QtCore.QDate.endOfDay
    -  PySide6.QtCore.QDate.getDate
    -  PySide6.QtCore.QDate.startOfDay
    """
    __slots__ = (
        '_date',
    )

    def __init__(self, year: int = None, month: int = None, day: int = None):
        self._date = QDate(year, month, day)

    @property
    def inner_object(self) -> QDate:
        return self._date

    @classmethod
    def from_string(cls, string: str, format: str) -> Date:
        """
        Returns the QDate represented by the string, using the format given, or an invalid date if the string cannot be parsed.

        +------+--------------------------------------------------------------------------------------------+
        | Expr | Output                                                                                     |
        +======+============================================================================================+
        | d    | The day as a number without a leading zero (1 to 31)                                       |
        +------+--------------------------------------------------------------------------------------------+
        | dd   | The day as a number with a leading zero (01 to 31)                                         |
        +------+--------------------------------------------------------------------------------------------+
        | ddd  | The abbreviated day name (‘Mon’ to ‘Sun’).                                                 |
        +------+--------------------------------------------------------------------------------------------+
        | dddd | The long day name (‘Monday’ to ‘Sunday’).                                                  |
        +------+--------------------------------------------------------------------------------------------+
        | M    | The month as a number without a leading zero (1 to 12)                                     |
        +------+--------------------------------------------------------------------------------------------+
        | MM   | The month as a number with a leading zero (01 to 12)                                       |
        +------+--------------------------------------------------------------------------------------------+
        | MMM  | The abbreviated month name (‘Jan’ to ‘Dec’).                                               |
        +------+--------------------------------------------------------------------------------------------+
        | MMMM | The long month name (‘January’ to ‘December’).                                             |
        +------+--------------------------------------------------------------------------------------------+
        | yy   | The year as a two digit number (00 to 99)                                                  |
        +------+--------------------------------------------------------------------------------------------+
        | yyyy | The year as a four digit number, possibly plus a leading minus sign for negative years.    |
        +------+--------------------------------------------------------------------------------------------+
        """
        date = QDate.fromString(string, format)
        obj = cls()
        obj._date = date
        return obj

    @classmethod
    def from_python_date(cls, date: datetime) -> Date:
        return cls(date.year, date.month, date.day)

    @classmethod
    def encapsulate(cls, date: QDate) -> Date:
        return cls(date.year(), date.month(), date.day())

    def to_python_date(self) -> datetime:
        return datetime(self._date.year(), self._date.month(), self._date.day())

    def add_days(self, days: int) -> Date:
        """
        Returns a QDate object containing a date ndays later than the date of this object (or earlier if ndays is negative).
        Returns a null date if the current date is invalid or the new date is out of range.
        """
        self._date.addDays(days)
        return self

    def add_months(self, months: int) -> Date:
        """
        Returns a QDate object containing a date nmonths later than the date of this object (or earlier if months is negative).
        """
        self._date.addMonths(months)
        return self

    def add_months_using_calendar(self, months: int, calendar: QCalendar) -> Date:
        """
        Returns a QDate object containing a date nmonths later than the date of this object (or earlier if nmonths is negative).

        Uses cal as calendar, if supplied, else the Gregorian calendar.
        """
        self._date.addMonths(months, calendar)
        return self

    def add_years(self, years: int) -> Date:
        """
        Returns a QDate object containing a date nyears later than the date of this object (or earlier if nyears is negative).
        """
        self._date.addYears(years)
        return self

    def add_years_using_calendar(self, years: int, calendar: QCalendar) -> Date:
        """
        Returns a QDate object containing a date nyears later than the date of this object (or earlier if nyears is negative).

        Uses cal as calendar, if supplied, else the Gregorian calendar.
        """
        self._date.addYears(years, calendar)
        return self

    @classmethod
    def current_date(cls) -> Date:
        """
        Returns the system clock’s current date.
        """
        return cls.encapsulate(QDate.currentDate())

    @property
    def day(self) -> int:
        """
        Returns the day of the month for this date.
        """
        return self._date.day()

    def get_day_using_calendar(self, calendar: QCalendar) -> int:
        """
        Returns the day of the month for this date.

        Uses cal as calendar if supplied, else the Gregorian calendar (for which the return ranges from 1 to 31). Returns 0 if the date is invalid.
        """
        return self._date.day(calendar)

    @property
    def day_of_week(self) -> QTDayOfWeek:
        """
        Returns the weekday (1 = Monday to 7 = Sunday) for this date.
        """
        return QTDayOfWeek(self._date.dayOfWeek())

    def day_of_week_using_calendar(self, calendar: QCalendar) -> QTDayOfWeek:
        """
        Returns the weekday (1 = Monday to 7 = Sunday) for this date.

        Uses cal as calendar if supplied, else the Gregorian calendar. Returns 0 if the date is invalid. Some calendars may give special meaning
        (e.g. intercallary days) to values greater than 7.
        """
        return QTDayOfWeek(self._date.dayOfWeek(calendar))

    @property
    def day_of_year(self) -> int:
        """
        Returns the day of the year (1 for the first day) for this date.
        """
        return self._date.dayOfYear()

    def day_of_year_using_calendar(self, calendar: QCalendar) -> int:
        """
        Returns the day of the year (1 for the first day) for this date.

        Uses cal as calendar if supplied, else the Gregorian calendar. Returns 0 if either the date or the first day of its year is invalid.
        """
        return self._date.dayOfYear(calendar)

    @property
    def number_of_days_in_month(self) -> int:
        """
        Returns the number of days in the month for this date.
        """
        return self._date.daysInMonth()

    def number_of_days_in_month_using_calendar(self, calendar: QCalendar) -> int:
        """
        Returns the number of days in the month for this date.

        Uses cal as calendar if supplied, else the Gregorian calendar (for which the result ranges from 28 to 31). Returns 0 if the date is invalid.
        """
        return self._date.daysInMonth(calendar)

    @property
    def number_of_days_in_year(self) -> int:
        """
        Returns the number of days in the year for this date.
        """
        return self._date.daysInYear()

    def number_of_days_in_year_using_calendar(self, calendar: QCalendar) -> int:
        """
        Returns the number of days in the year for this date.

        Uses cal as calendar if supplied, else the Gregorian calendar (for which the result is 365 or 366). Returns 0 if the date is invalid.
        """
        return self._date.daysInYear(calendar)

    def diff_in_days_qdate(self, date: QDate) -> int:
        """
        Returns the number of days from this date to d (which is negative if d is earlier than this date).

        Returns 0 if either date is invalid.
        """
        return self._date.daysTo(date)

    def diff_in_days_py(self, date: datetime) -> int:
        """
        Returns the number of days from this date to d (which is negative if d is earlier than this date).

        Returns 0 if either date is invalid.
        """
        return self._date.daysTo(QDate(date.year, date.month, date.day))

    @property
    def is_leap_year(self) -> bool:
        """
        Returns true if the specified year is a leap year in the Gregorian calendar; otherwise returns false.
        """
        return self._date.isLeapYear(self._date.year())

    @property
    def is_null(self) -> bool:
        """
        Returns true if the date is null; otherwise returns false. A null date is invalid.
        """
        return self._date.isNull()

    @property
    def is_valid(self) -> bool:
        """
        Returns true if this date is valid; otherwise returns false.
        """
        return self._date.isValid()

    @staticmethod
    def is_date_valid(year: int, month: int, day: int) -> bool:
        """
        Returns true if the specified date (year, month, and day) is valid in the Gregorian calendar; otherwise returns false.
        """
        return QDate.isValid(year, month, day)

    @property
    def month(self) -> QTMonth:
        """
        Returns the month-number for the date.
        """
        return QTMonth(self._date.month())

    def get_month_using_calendar(self, calendar: QCalendar) -> int:
        """
        Returns the month-number for the date.

        Numbers the months of the year starting with 1 for the first. Uses cal as calendar if supplied, else the Gregorian calendar
        """
        return QTMonth(self._date.month(calendar))

    def set_date(self, year: int, month: int, day: int, calendar: QCalendar = None) -> Date:
        """
        Sets this to represent the date, in the given calendar cal, with the given year, month and day numbers. Returns true if the resulting date is
        valid, otherwise it sets this to represent an invalid date and returns false.
        """
        if calendar:
            self._date.setDate(year, month, day, calendar)
        else:
            self._date.setDate(year, month, day)
        return self

    def to_string(self, format: str = None) -> str:
        """
        Returns the date as a string. The format parameter determines the format of the string.

        If the format is ISODate , the string format corresponds to the ISO 8601 extended specification for representations of dates and times,
        taking the form yyyy-MM-dd, where yyyy is the year, MM is the month of the year (between 01 and 12), and dd is the day of the month between
        01 and 31.

        If the format is RFC2822Date , the string is formatted in an RFC 2822 compatible way. An example of this formatting is “20 May 1995”.

        +------+--------------------------------------------------------------------------------------------+
        | Expr | Output                                                                                     |
        +======+============================================================================================+
        | d    | The day as a number without a leading zero (1 to 31)                                       |
        +------+--------------------------------------------------------------------------------------------+
        | dd   | The day as a number with a leading zero (01 to 31)                                         |
        +------+--------------------------------------------------------------------------------------------+
        | ddd  | The abbreviated day name (‘Mon’ to ‘Sun’).                                                 |
        +------+--------------------------------------------------------------------------------------------+
        | dddd | The long day name (‘Monday’ to ‘Sunday’).                                                  |
        +------+--------------------------------------------------------------------------------------------+
        | M    | The month as a number without a leading zero (1 to 12)                                     |
        +------+--------------------------------------------------------------------------------------------+
        | MM   | The month as a number with a leading zero (01 to 12)                                       |
        +------+--------------------------------------------------------------------------------------------+
        | MMM  | The abbreviated month name (‘Jan’ to ‘Dec’).                                               |
        +------+--------------------------------------------------------------------------------------------+
        | MMMM | The long month name (‘January’ to ‘December’).                                             |
        +------+--------------------------------------------------------------------------------------------+
        | yy   | The year as a two digit number (00 to 99)                                                  |
        +------+--------------------------------------------------------------------------------------------+
        | yyyy | The year as a four digit number, possibly plus a leading minus sign for negative years.    |
        +------+--------------------------------------------------------------------------------------------+
        """
        return self._date.toString(format)

    @property
    def week_number(self) -> int:
        """
        Returns the ISO 8601 week number (1 to 53).
        """
        return self._date.weekNumber()

    @property
    def year(self) -> int:
        """
        Returns the year of this date.
        """
        return self._date.year()

    def get_year_using_calendar(self, calendar: QCalendar) -> int:
        """
        Returns the year of this date.

        Uses cal as calendar, if supplied, else the Gregorian calendar.
        """
        return self._date.year(calendar)

    def __reduce__(self):
        return self._date.__reduce__()

    def __repr__(self) -> str:
        return self._date.__repr__()

    def __ne__(self, other) -> bool:
        return self._date.__ne__(other)

    def __lt__(self, other) -> bool:
        return self._date.__lt__(other)

    def __le__(self, other) -> bool:
        return self._date.__le__(other)

    def __eq__(self, other) -> bool:
        return self._date.__eq__(other)

    def __gt__(self, other) -> bool:
        return self._date.__gt__(other)

    def __ge__(self, other) -> bool:
        return self._date.__ge__(other)





if __name__ == '__main__':
    d = Date(2000, 10, 1)
    print(repr(d))
