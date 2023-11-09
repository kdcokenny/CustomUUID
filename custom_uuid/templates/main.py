from ..main import generate_custom_uuid


def uuid_with_date() -> str:
    return generate_custom_uuid(
        include_date=True, date_format="%Y%m%d", separator="-", max_length=None
    )


def uuid_for_app(app_id: str) -> str:
    return generate_custom_uuid(
        app_id,
        include_date=True,
        date_format="%Y%m%d",
        separator="-",
        max_length=None,
    )


def compact_uuid() -> str:
    return generate_custom_uuid(
        include_date=False, separator="", max_length=32
    )


def uuid_with_custom_elements(
    *values: str, include_date: bool = True, date_format: str = "%Y%m%d"
) -> str:
    return generate_custom_uuid(
        *values,
        include_date=include_date,
        date_format=date_format,
        separator="-",
        max_length=None
    )


def timestamped_uuid() -> str:
    return generate_custom_uuid(
        include_date=True,
        date_format="%Y%m%d%H%M%S",
        separator="-",
        max_length=None,
    )
