from django.test import TestCase
from django.utils import timezone
from freezegun import freeze_time

from django_jalalify import JalaliDatetime
from django_jalalify.timezone import TEHRAN_ZONE, TehranTimezone


class TehranTimezoneTestCase(TestCase):

    @freeze_time("2023-5-3 10:45:36.466402", tz_offset=0)
    def test_jalali_tehran_timezone_correctness_of_dst_with_custom_tehrantimezone(self):
        must_be_jalali_in_tehran = "1402/02/13 14:15:36.466402"
        now = JalaliDatetime.now()
        now_in_jalali_and_tehran_timezone = now.astimezone(TehranTimezone()).strftime("%Y/%m/%d %H:%M:%S.%f")
        self.assertEqual(now_in_jalali_and_tehran_timezone, must_be_jalali_in_tehran)

    @freeze_time("2023-05-03 10:45:36.466402", tz_offset=0)
    def test_tehran_timezone_correctness_of_dst_with_checkout_casting(self):
        must_be_in_tehran = "2023/05/03 14:15:36.466402"
        now = timezone.now()
        now_in_tehran_timezone = now.astimezone(TEHRAN_ZONE).strftime("%Y/%m/%d %H:%M:%S.%f")
        self.assertEqual(now_in_tehran_timezone, must_be_in_tehran)

    def test_tehran_timezone_correctness_of_dst(self):
        now = timezone.now()
        now_casting_checkout_app = now.astimezone(TEHRAN_ZONE).strftime("%Y/%m/%d %H:%M:%S.%f")
        now_casting_with_custom_tehran_timezone = now.astimezone(TehranTimezone()).strftime(
            "%Y/%m/%d %H:%M:%S.%f")
        self.assertEqual(now_casting_checkout_app, now_casting_with_custom_tehran_timezone)
