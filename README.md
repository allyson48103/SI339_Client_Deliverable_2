# SI339_Client_Deliverable_2
Client Project Deliverable 2 - HTML Content


Athlete Race Data to HTML Generator
Overview
This Python script reads an athlete's race data from a CSV file and generates an HTML file that displays the data in a table format. The script is designed to work with any CSV file formatted with the required fields, and it automatically creates a structured HTML output file with the athlete's name and race performance details, including photos (if provided).

How It Works
Input CSV File: The script takes a CSV file as input. The CSV file must have the following format:

The first row contains the athlete's name.
The second row contains the athlete's ID.
Subsequent rows contain race data with the following columns:
Name: Athlete's name.
Overall Place: The position of the athlete in the race.
Grade: Athlete's grade level during the race.
Time: Time taken to complete the race.
Date: Date of the race.
Meet: The name of the race or event.
Comments: Comments or feedback on the race.
Photo: The file name of the athlete's photo (optional).
HTML File Generation: The script generates an HTML file based on the CSV data. The output file contains:

A title and heading with the athlete's name.
The athlete's ID displayed in a paragraph.
A table with columns for each race's details, including an image if a photo is provided.
Output: The generated HTML file will be named using the athlete's name (e.g., AthleteName_RaceData.html).

