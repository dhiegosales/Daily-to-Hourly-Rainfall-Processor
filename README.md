# Daily2HourRain: Daily to Hourly Rainfall Processor

Welcome to the **Daily2HourRain** Python program! This tool processes a CSV file containing daily rainfall data and converts it into hourly rainfall data by linearly estimating hourly values from the daily data.

## Table of Contents

- [Overview](#overview)
- [Input Requirements](#input-requirements)
- [Output](#output)
- [Executable for Windows](#executable-for-windows)
- [Usage](#usage)
- [Example File](#example-file)
- [Author](#author)
- [Contact](#contact)

## Overview

**Daily2HourRain** is a Python program designed to convert daily precipitation data into hourly estimates. It achieves this by dividing the daily precipitation value by 24, thereby providing hourly estimates throughout the day.

## Input Requirements

- **Input File**: The program requires a CSV file named `daily_rainfall.csv` as input.
- **Format**: The input CSV file should be structured with data separated by semicolons (`;`):

Date;Station1;Station2;Station3;...

dd/mm/yyyy;float;float;float;..


- **Date**: The first column must contain dates in the format `dd/mm/yyyy`.
- **Station Columns**: Subsequent columns should contain numeric values representing daily rainfall data for each station.

## Output

- **Output File**: Upon successful processing, the program generates an output CSV file named `hourly_rainfall.csv`.
- **Format**: The output file will have the following structure:

Date_hourly;Station1_hourly;Station2_hourly;Station3_hourly;...

dd/mm/yyyy hh;float;float;float;..


- **Date_hourly**: Each row corresponds to hourly data derived from the daily data provided in the input file.

## Executable for Windows

- **Executable**: You can download a pre-built executable for Windows 64-bit from the repository.
- **Usage**: Ensure the executable (`Daily2HourRain.exe`) is placed in the same directory as your `daily_rainfall.csv` input file.

## Usage

1. **Download**: Download the repository including the executable (`Daily2HourRain.exe`) and the `daily_rainfall.csv` input file.

2. **Execution**: Double-click on `Daily2HourRain.exe` to run the program.

3. **Output**: The program will automatically process the `daily_rainfall.csv` file and generate `hourly_rainfall.csv` in the same directory.

## Example File

- **Example**: An example `daily_rainfall.csv` file will be provided alongside as a sample.

### Example 
`daily_rainfall.csv`

|Date        | Station1 | Station2 | Station3 | ... |
|-------------|----------|----------|----------|----|
| 01/06/2024  | 10       | 15       | 8        |... |
| 02/06/2024  | 5        | 12       | 6        |... |
| ...         | ...      | ...      | ...      |... |

`hourly_rainfall.csv`

| Date_hourly      | Station1_hourly | Station2_hourly | Station3_hourly |
|------------------|-----------------|-----------------|-----------------|
| 01/06/2024 00:00 | 0.4167          | 0.625           | 0.3333          |
| 01/06/2024 01:00 | 0.4167          | 0.625           | 0.3333          |
| 01/06/2024 02:00 | 0.4167          | 0.625           | 0.3333          |
| ...              | ...             | ...             | ...             |
| 01/06/2024 23:00 | 0.4167          | 0.625           | 0.3333          |
| 02/06/2024 00:00 | 0.2083          | 0.5             | 0.25            |
| 02/06/2024 01:00 | 0.2083          | 0.5             | 0.25            |
| 02/06/2024 02:00 | 0.2083          | 0.5             | 0.25            |
| ...              | ...             | ...             | ...             |
| 02/06/2024 23:00 | 0.2083          | 0.5             | 0.25            |
| ...              | ...             | ...             | ...             |

## Author

- **Dhiego da Silva Sales**
- **Affiliation**: Instituto Federal Fluminense
- **Contact**: dhiego.sales@outlook.com


