from django.core.exceptions import ValidationError
from django.forms import DateTimeField
from django.forms.utils import from_current_timezone
from django.utils.translation import gettext_lazy as _
from django_filters import fields, widgets

from django_jalalify import JalaliDate, JalaliDatetime


class JalaliDateTimeField(DateTimeField):
    default_error_messages = {
        "invalid": _("Enter a valid datetime of the format YYY/mm/dd HH:MM:SS."),
    }

    def to_python(self, value):
        """
        method used to convert the input value into datetime. currently, the only supported format is YYYY/mm/DD HH:MM/SS
        :param value: str
        :return: datetime. timezone aware instance
        """
        if value in self.empty_values:
            return None
        try:
            dt = JalaliDatetime.strptime(value, "%Y/%m/%d %H:%M:%S").todatetime()
        except (ValueError, TypeError):
            raise ValidationError(message={"datetime_jalali": [self.error_messages["invalid"]]}, code="invalid")
        return from_current_timezone(dt)


class JalaliDateField(DateTimeField):
    def to_python(self, value):
        """
        method used to convert the input value into date. The only supported format is YYYY/mm/DD
        :param value: str
        :return: date.
        """
        if value in self.empty_values:
            return None
        try:
            dt = JalaliDate.strptime(value, "%Y/%m/%d").todate()
        except (ValueError, TypeError):
            raise ValidationError(self.error_messages["invalid"], code="invalid")
        return dt


class JalaliDateRangeField(fields.RangeField):
    widget = widgets.DateRangeWidget

    def __init__(self, *args, **kwargs):
        fields = (
            JalaliDateField(),
            JalaliDateField(),
        )
        super().__init__(fields, *args, **kwargs)


class JalaliDateTimeRangeField(fields.RangeField):
    widget = widgets.DateRangeWidget

    def __init__(self, *args, **kwargs):
        fields = (
            JalaliDateTimeField(),
            JalaliDateTimeField(),
        )
        super().__init__(fields, *args, **kwargs)
