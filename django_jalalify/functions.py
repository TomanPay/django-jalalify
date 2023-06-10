def convert_date_to_int(date) -> int:
    return int(str(date).replace("-", "")[:8])


def convert_time_to_int(time_string) -> int:
    return int(str(time_string).replace(":", "")[0:6])


def int_of_time_to_str(time) -> str:
    return f"{time:06d}"
