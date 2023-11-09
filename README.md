# CustomUUID

CustomUUID is a versatile UUID generation library designed to create unique identifiers with optional embedded information such as dates or custom values. It's ideal for applications requiring unique IDs with additional embedded context.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)


## Introduction

CustomUUID provides a flexible way to generate UUIDs (Universally Unique Identifiers) with optional embedding of dates, application-specific IDs, or other relevant data. It supports various customization levels, from simple UUIDs to complex ones containing multiple data types.

## Features

- **Standard UUID Generation:** Generate regular UUIDs compliant with RFC 4122.
- **Date Embedding:** Option to embed the current date into the UUID for temporal context.
- **Custom Value Embedding:** Embed up to three custom values into the UUID for additional context.
- **Length Management:** Automatically handles the length of UUIDs to ensure they stay within standard limits.
- **Predefined Templates:** Includes several template functions for common use cases, facilitating ease of use.

## Installation

To install CustomUUID, run the following command:

```bash
pip install custom_uuid
```

## Usage

Basic usage example:

```python
from customuuid import create_uuid

# Generate a standard UUID
uuid = create_uuid()
print(uuid)
```

Advanced usage with custom values:

```python
from customuuid import create_custom_uuid

# Generate a UUID with custom values
uuid = create_custom_uuid(include_date=True, custom_values=["app_id", "user_id"])
print(uuid)
```

## Configuration

CustomUUID allows various configurations to tailor the UUID generation to your specific needs. Refer to the documentation for detailed configuration options.

## License

CustomUUID is licensed under the MIT License.