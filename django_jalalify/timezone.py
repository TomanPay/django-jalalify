# -*- coding: utf-8 -*-
from datetime import tzinfo, timedelta, datetime

import pytz
from khayyam.helpers import force_encoded_string_output

ZERO_DELTA = timedelta(0)
TEHRAN_OFFSET = timedelta(hours=3, minutes=30)

TEHRAN_LMT_ZONE = pytz.timezone("Asia/Tehran")
TEHRAN_ZONE = datetime(2000, 1, 1).astimezone(pytz.timezone("Asia/Tehran")).tzinfo


class Timezone(tzinfo):

    def __init__(self, offset, name=None):
        assert (isinstance(offset, timedelta))
        self._offset = offset
        self._name = name
        super(Timezone, self).__init__()

    def fromutc(self, dt):
        if dt.tzinfo is None:
            raise ValueError('The object: %s is naive.' % dt)

        if dt.tzinfo != self:
            raise ValueError('Datetime timezone mismatch: %s != %s' % (dt.tzinfo, self))

        utc_offset = dt.utcoffset()
        delta = utc_offset

        if delta:
            dt += delta  # convert to standard local time

        return dt

    def utcoffset(self, dt):
        return self._offset

    def dst(self, dt):
        return ZERO_DELTA

    def __unicode__(self):
        off = self._offset
        return '%s%.2d:%.2d' % (
            '+' if off.total_seconds() >= 0 else '-',
            int(off.total_seconds() / 3600),
            int((off.total_seconds() % 3600) / 60),
        )

    __repr__ = force_encoded_string_output(__unicode__)

    def tzname(self, dt):
        if self._name:
            return self._name
        else:
            return repr(self)

    def __hash__(self):
        return hash(self._offset)


class TehranTimezone(Timezone):
    """
    Tehran timezone with a fixed +3:30 GMT offset.
    """

    def __init__(self):
        super(TehranTimezone, self).__init__(
            TEHRAN_OFFSET,
            "Asia/Tehran"
        )
