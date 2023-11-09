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

### Basic Usage Examples with Sample Outputs

1. **Generating a Standard UUID:**
   ```python
   import custom_uuid

   standard_uuid = custom_uuid.generate_custom_uuid()
   print("Standard UUID:", standard_uuid)
   ```
   Output:
   ```
   Standard UUID: 123e4567-e89b-12d3-a456-426614174000
   ```

2. **Generating a UUID with Current Date:**
   ```python
   date_uuid = custom_uuid.uuid_with_date()
   print("UUID with Date:", date_uuid)
   ```
   Output:
   ```
   UUID with Date: 20231109-123e4567-e89b-12d3-a456-426614174000
   ```

3. **Generating a UUID for a Specific Application:**
   ```python
   app_uuid = custom_uuid.uuid_for_app("MyApp123")
   print("UUID for App:", app_uuid)
   ```
   Output:
   ```
   UUID for App: MyApp123-20231109-123e4567-e89b-12d3-a456-426614174000
   ```

4. **Generating a Compact UUID Without Separators:**
   ```python
   compact_uuid = custom_uuid.compact_uuid()
   print("Compact UUID:", compact_uuid)
   ```
   Output:
   ```
   Compact UUID: 123e4567e89b12d3a456426614174000
   ```

5. **Generating a UUID with Custom Elements:**
   ```python
   custom_elements_uuid = custom_uuid.uuid_with_custom_elements("Element1", "Element2")
   print("UUID with Custom Elements:", custom_elements_uuid)
   ```
   Output:
   ```
   UUID with Custom Elements: Element1-Element2-20231109-123e4567-e89b-12d3-a456-426614174000
   ```

6. **Generating a Timestamped UUID:**
   ```python
   timestamped_uuid = custom_uuid.timestamped_uuid()
   print("Timestamped UUID:", timestamped_uuid)
   ```
   Output:
   ```
   Timestamped UUID: 20231109123000-123e4567-e89b-12d3-a456-426614174000
   ```

## Configuration

CustomUUID allows various configurations to tailor the UUID generation to your specific needs. Refer to the documentation for detailed configuration options.

## License

CustomUUID is licensed under the MIT License.