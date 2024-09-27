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


'''
Project Title: "Historical Weather Data Retrieval and CSV Export for Boston (May 2024 - August 2024)"
Objective:
The purpose of this project is to retrieve historical weather data for the city of Boston between May 1st, 2024, and August 31st, 2024, and store the information in a CSV file for further analysis. The project demonstrates how to utilize a public API, process data, and export it to a structured format (CSV) for future use.

Steps and Explanation:
API Selection and Data Retrieval:

API Used: The Open-Meteo API, which provides historical weather data, was selected for this project.
Data Location: The project focuses on Boston, using its latitude and longitude coordinates (42.3601, -71.0589) to query the API.
Timeframe: The data is retrieved for the period from May 1st, 2024, to August 31st, 2024.
Weather Variables: The data includes daily maximum and minimum temperatures, precipitation amounts, and maximum wind speeds.
Data Processing:

A GET request was sent to the API, and the returned data was converted into JSON format, which is a structured format commonly used in web APIs.
The relevant weather details were extracted from the API’s response.
CSV File Generation:

The weather data was written to a CSV (Comma-Separated Values) file for easy access and further analysis.
The CSV file includes columns for the date, maximum and minimum temperatures, precipitation, and maximum wind speed.
Code Implementation:

Python was used as the programming language for its simplicity and powerful libraries like requests (to interact with the API) and csv (to write the data to a CSV file).
Error handling was incorporated to ensure the API request was successful before processing the data.
The final output was a CSV file named boston_weather_data.csv containing the historical weather data.
Challenges Faced:

Understanding the API's documentation to extract the correct data fields.
Handling different weather attributes and ensuring the correct time zone for Boston's weather data.
Key Learnings:
How to interact with a public API to retrieve data.
Converting JSON data to a format suitable for storage (CSV).
Writing Python code to automate the process of fetching and exporting data.
Handling various weather attributes and ensuring accuracy in data retrieval.
Future Enhancements:
Automating the data retrieval process to gather real-time weather data.
Extending the project to analyze the weather patterns over time using statistical methods or data visualization.
Incorporating additional weather attributes, such as humidity or cloud cover, to provide a more comprehensive analysis.
'''

# '''
# Let's say you want to get some data from a website or API. The requests library can be used to fetch data, 
# for example, retrieving data from a public API that provides weather information.
# '''

# # First we need to import the "request" library
# import requests
# import csv

# # Define the API endpoint (a public weather API in this case)
# # Get data from the historical weather API for Boston
# # Latitude and longitude for Boston: 42.3601 (lat), -71.0589 (lon)
# url = "https://archive-api.open-meteo.com/v1/archive?latitude=42.3601&longitude=-71.0589&start_date=2024-05-01&end_date=2024-08-31&daily=temperature_2m_max,temperature_2m_min,precipitation_sum,windspeed_10m_max&timezone=America/New_York"

# # Send GET request to the server to fetch data 
# response = requests.get(url) # Sends a GET request to the specified URL to retrieve data. You can also use POST, PUT, DELETE methods, etc., depending on your need.

# # The server sends back response which we can check i.e check if the request was successful
# if response.status_code == 200:
#     data = response.json() # Converts the response into JSON format (key value pair) and when we use response.json(), Python automatically interprets it as a dictionary and we know data has data type of dictionary.
#     print(type(date))
    
#     # extract the relevant info from the json reponse
#     weather_data = data['current_weather']

# # Open a csv file and write the data
#     with open('weather_data.csv', mode='w', newline='') as file:
#         writer = csv.writer(file)

#     # Write the header/column names
#         writer.writerow(['Temperature (\u00B0;C)', 'Wind Speed (km/h)', 'Wind Direction', 'Weather Code', 'Time'])

#     # write data to the csv file
#         writer.writeow([weather_data['temperature'], weather_data['windspeed'], weather_data['winddirection'], 
#                     weather_data['weathercode'],data['current_weather']['time']])

#     print("Data has been written to weather_data.csv")
# else:
#     print("Failed to retrieve data. Status Coed:", response.status_code)/





