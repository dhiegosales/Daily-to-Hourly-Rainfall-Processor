# Daily-to-Hourly-Rainfall-Processor

This Python script processes a CSV file containing daily rainfall data and converts it into hourly rainfall data.

## How It Works

1. **Date Conversion:** The script converts dates from the format `dd/mm/yyyy` to `dd/mm/yyyy hh:min` for each hour of the day (00:00 to 23:00).
2. **Rainfall Distribution:** The script distributes the daily rainfall value evenly across 24 hours to generate hourly rainfall data. This is achieved by dividing the daily rainfall value by 24.
3. **CSV Processing:** The processed data is written to a new CSV file.

## Input File Format

The input CSV file should have the following format:
- The first row should contain headers.
- The first column contains dates in the format `dd/mm/yyyy`.
- The subsequent columns contain daily rainfall values.

### Example Input (`input_data.csv`)

| date       | rainfall1 | rainfall2 |
|------------|-----------|-----------|
| 01/01/2024 | 12.0      | 15.5      |
| 02/01/2024 | 8.0       | 10.0      |

## Output File Format

The output CSV file will have the following format:
- The first row will contain headers indicating hourly data.
- The first column contains dates and times in the format `dd/mm/yyyy hh:min`.
- The subsequent columns contain hourly rainfall values.

### Example Output (`output_data.csv`)

#### 01/01/2024

| date_time          | rainfall1_hourly | rainfall2_hourly |
|--------------------|------------------|------------------|
| 01/01/2024 00:00   | 0.5              | 0.6458333333333334 |
| 01/01/2024 01:00   | 0.5              | 0.6458333333333334 |
| 01/01/2024 02:00   | 0.5              | 0.6458333333333334 |
| 01/01/2024 03:00   | 0.5              | 0.6458333333333334 |
| 01/01/2024 04:00   | 0.5              | 0.6458333333333334 |
| 01/01/2024 05:00   | 0.5              | 0.6458333333333334 |
| 01/01/2024 06:00   | 0.5              | 0.6458333333333334 |
| 01/01/2024 07:00   | 0.5              | 0.6458333333333334 |
| 01/01/2024 08:00   | 0.5              | 0.6458333333333334 |
| 01/01/2024 09:00   | 0.5              | 0.6458333333333334 |
| 01/01/2024 10:00   | 0.5              | 0.6458333333333334 |
| 01/01/2024 11:00   | 0.5              | 0.6458333333333334 |
| 01/01/2024 12:00   | 0.5              | 0.6458333333333334 |
| 01/01/2024 13:00   | 0.5              | 0.6458333333333334 |
| 01/01/2024 14:00   | 0.5              | 0.6458333333333334 |
| 01/01/2024 15:00   | 0.5              | 0.6458333333333334 |
| 01/01/2024 16:00   | 0.5              | 0.6458333333333334 |
| 01/01/2024 17:00   | 0.5              | 0.6458333333333334 |
| 01/01/2024 18:00   | 0.5              | 0.6458333333333334 |
| 01/01/2024 19:00   | 0.5              | 0.6458333333333334 |
| 01/01/2024 20:00   | 0.5              | 0.6458333333333334 |
| 01/01/2024 21:00   | 0.5              | 0.6458333333333334 |
| 01/01/2024 22:00   | 0.5              | 0.6458333333333334 |
| 01/01/2024 23:00   | 0.5              | 0.6458333333333334 |
| 02/01/2024 00:00   | 0.3333333333333333 | 0.4166666666666667 |
| 02/01/2024 01:00   | 0.3333333333333333 | 0.4166666666666667 |
| 02/01/2024 02:00   | 0.3333333333333333 | 0.4166666666666667 |
| 02/01/2024 03:00   | 0.3333333333333333 | 0.4166666666666667 |
| 02/01/2024 04:00   | 0.3333333333333333 | 0.4166666666666667 |
| 02/01/2024 05:00   | 0.3333333333333333 | 0.4166666666666667 |
| 02/01/2024 06:00   | 0.3333333333333333 | 0.4166666666666667 |
| ...                | ...              | ...              |

Each daily rainfall value is evenly distributed across 24 hours to calculate hourly values.

## How to Use

1. Ensure you have Python installed on your system.
2. Place your input CSV file in the same directory as the script.
3. Run the script using the following command:

```bash
python process_csv.py
The script will read the input CSV file input_data.csv and generate the output CSV file output_data.csv.
```

## Functions

### `convert_date(date_str, hour)`

Converts a date from `dd/mm/yyyy` format to `dd/mm/yyyy hh:min` format for a given hour.

- `date_str` (str): The date string in `dd/mm/yyyy` format.
- `hour` (int): The hour to be set in the converted date.

### `process_csv(input_file, output_file)`

Processes the input CSV file, converting daily rainfall data to hourly rainfall data, and writes the output to a new CSV file.

- `input_file` (str): The path to the input CSV file.
- `output_file` (str): The path to the output CSV file.
