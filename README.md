# Boston Weather Insights: Data Retriever

## Overview

Boston Weather Insights is a Python-based tool designed to retrieve historical weather data for Boston, Massachusetts, from May 1st, 2024, to August 31st, 2024. The project leverages the Open-Meteo API to fetch daily weather metrics such as temperature, precipitation, and wind speed, and exports them to a CSV file for easy analysis.

## Features

- Fetches historical weather data for Boston (42.3601° N, 71.0589° W)
- Covers a 4-month period (May 1, 2024 - August 31, 2024)
- Retrieves daily maximum and minimum temperatures, precipitation, and maximum wind speed
- Outputs data in CSV format for further analysis

## Requirements

- Python 3.6+
- `requests` library (install via `pip`)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/boston-weather-insights.git
   ```

2. Navigate to the project directory:
   ```bash
   cd boston-weather-insights
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the script, execute the following command in your terminal:

```bash
python weather_data_retriever.py
```

The script will generate a CSV file named `boston_weather_data.csv` in the project directory.

## CSV File Structure

The generated CSV file contains the following columns:

- Date
- Max Temperature (°C)
- Min Temperature (°C)
- Precipitation (mm)
- Max Wind Speed (km/h)

## API Information

This project uses the Open-Meteo API to retrieve historical weather data. For more information, visit the [Open-Meteo API website](https://open-meteo.com/).

## Future Enhancements

- Support for real-time weather data retrieval
- Data visualization features (e.g., graphs, plots)
- Extend the date range for long-term historical weather data analysis
- Include additional weather attributes (e.g., humidity, cloud cover)

## Contributing

Contributions are welcome! If you'd like to contribute, please submit a Pull Request with your proposed changes.

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE.txt) file for details.


