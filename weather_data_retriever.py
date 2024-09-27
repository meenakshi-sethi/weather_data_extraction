# Weather Data Retrieval

# improting libraries
import requests
import csv

# Step 1: Define the API endpoint (for historical weather data for Boston)
# Latitude and longitude for Boston 42.3601 (lat), -71.0589 (lon)

url = "https://archive-api.open-meteo.com/v1/archive?latitude=42.3601&longitude=-71.0589&start_date=2024-05-01&end_date=2024-08-31&daily=temperature_2m_max,temperature_2m_min,precipitation_sum,windspeed_10m_max&timezone=America/New_York"

# Step 2: Send GET request to the server to fetch data
response = requests.get(url)

# Step 3: Check if the request was successful
if response.status_code == 200:
    data = response.json() # Convert the response to JSON format (returns a python dictionary)

    # Extract the relevant information from the JSON response (daily weather data)
    daily_data = data['daily']

    # Step 4 Open cvs file and write the data
    with open('boston_weather_data.csv', mode = 'w', newline = '') as file:
        writer = csv.writer(file)

        #Step 5: Write the header (column names)
        writer.writerow(['Date', 'Max Temp (c)', 'Min Temp (c)', 'Percipitation (mm)', 'Max Wind Speed (Km/h)'])

        # Step 6: Write the daily weather data to the CSV file
        for i in range(len(daily_data['time'])):
            writer.writerow([
            daily_data['time'][i],
            daily_data['temperature_2m_max'][i],
            daily_data['temperature_2m_min'][i],
            daily_data['precipitation_sum'][i],
            daily_data['windspeed_10m_max'][i],    
            ])
    print("Data Has been written to boston_weather_data.csv")
else:
    print("Failed to retrieve data. Status Code:", response.status_code)

