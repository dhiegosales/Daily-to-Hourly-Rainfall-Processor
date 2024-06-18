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

| date_time          | rainfall1_hourly | rainfall2_hourly |
|--------------------|------------------|------------------|
| 01/01/2024 00:00   | 0.5              | 0.6458333333333334 |
| 01/01/2024 01:00   | 0.5              | 0.6458333333333334 |
| ...                | ...              | ...              |

Each daily rainfall value is evenly distributed across 24 hours to calculate hourly values.

## How to Use

1. Ensure you have Python installed on your system.
2. Place your input CSV file in the same directory as the script.
3. Run the script using the following command:

```bash
python process_csv.py
