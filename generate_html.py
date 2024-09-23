import csv
import os

def generate_html_from_csv(csv_filename):
    # Extract the athlete's name and ID from the first row in the CSV file
    with open(csv_filename, 'r') as file:
        reader = csv.reader(file)
        # Read first two rows for the athlete's name and ID
        athlete_name = next(reader)[0]
        athlete_id = next(reader)[0]

    # Define the name of the HTML file based on the athlete's name
    output_filename = f"{athlete_name.replace(' ', '_')}_RaceData.html"

    # Open the CSV again to process the entire file
    with open(csv_filename, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)[2:]  # Skip the first two lines with name and ID
    
    # Create the HTML content
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{athlete_name}'s Race Data</title>
</head>
<body>
    <h1>{athlete_name}'s Race Data</h1>
    <p>Athlete ID: {athlete_id}</p>
    <table border="1">
        <thead>
            <tr>
                <th>Name</th>
                <th>Overall Place</th>
                <th>Grade</th>
                <th>Time</th>
                <th>Date</th>
                <th>Meet</th>
                <th>Comments</th>
                <th>Photo</th>
            </tr>
        </thead>
        <tbody>"""

    # Loop through the CSV data and generate table rows
    for row in data:
        html_content += f"""
            <tr>
                <td>{row[0]}</td>
                <td>{row[1]}</td>
                <td>{row[2]}</td>
                <td>{row[3]}</td>
                <td>{row[4]}</td>
                <td>{row[5]}</td>
                <td>{row[6]}</td>
                <td><img src="{row[7]}" alt="{athlete_name}'s Photo" width="100"></td>
            </tr>"""
    
    # Close the HTML tags
    html_content += """
        </tbody>
    </table>
</body>
</html>"""

    # Write the HTML content to a file
    with open(output_filename, 'w') as output_file:
        output_file.write(html_content)
    
    print(f"HTML file generated: {output_filename}")

# Replace 'athlete_data.csv' with your CSV filename
generate_html_from_csv('athlete_data.csv')
