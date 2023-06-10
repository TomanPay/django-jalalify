from typing import Union

from django_jalalify import JalaliDatetime
from django_jalalify.timezone import TEHRAN_ZONE


class FieldDateTimeInJalaliGeneratorMixin:

    def _field_datetime_in_jalali(self, field_name) -> Union[None, str]:
        field_object = self._meta.get_field(field_name)
        field_value = field_object.value_from_object(self)
        return field_value and JalaliDatetime(field_value.astimezone(TEHRAN_ZONE)).strftime(
            "%Y/%m/%d %H:%M:%S"
        )
