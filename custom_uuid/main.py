import uuid
from datetime import datetime
from typing import Optional


def generate_custom_uuid(
    *values: Optional[str],
    include_date: bool = True,
    date_format: str = "%Y%m%d",
    separator: str = "-",
    max_length: Optional[int] = None
) -> str:
    parts = list(filter(None, values))

    if include_date:
        current_date = datetime.now().strftime(date_format)
        parts.append(current_date)

    unique_uuid = str(uuid.uuid4())
    parts.append(unique_uuid)

    custom_uuid = separator.join(parts)

    if max_length and len(custom_uuid) > max_length:
        custom_uuid = custom_uuid[:max_length]

    return custom_uuid
