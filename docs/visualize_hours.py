import matplotlib.pyplot as plt
from collections import defaultdict
import re
from datetime import datetime

# Helper function to parse markdown and extract the table data line by line
def extract_sprint_data_from_lines(lines):
    data = defaultdict(list)  # To store data grouped by Name
    all_hours = defaultdict(list)  # To store 'All' hours for each date

    # Updated regex to handle spaces around the columns
    row_pattern = re.compile(r'\|?\s*(\d{4}-\d{2}-\d{2})\s*\|\s*([\d\.]+)\s*\|\s*([\w\s]+)\s*\|')

    for line in lines:
        line = line.strip()  # Remove leading/trailing whitespace
        match = row_pattern.search(line)  # Search for the table pattern anywhere in the line

        if match:
            date_str, hours_str, name = match.groups()
            date = datetime.strptime(date_str, '%Y-%m-%d')
            hours = float(hours_str) if hours_str else 0

            # Normalize names to avoid duplicates (e.g., "Nate Stott" -> "Nate")
            normalized_name = normalize_name(name)

            if normalized_name.lower() == 'all':  # Special case for 'All' category
                all_hours[date].append(hours)
            else:
                data[normalized_name].append((date, hours))

    return data, all_hours

def normalize_name(name):
    """Normalize name for consistency (e.g., Nate Stott -> Nate)"""
    name = name.strip().lower()
    return name.title()  # Capitalize the name properly

# Helper function to aggregate hours worked across duplicate entries (same person on the same date)
def aggregate_data(data, all_hours):
    aggregated_data = defaultdict(list)

    # Add 'All' hours to each person's data
    for name, records in data.items():
        # Aggregate hours by date for each person
        current_date = None
        total_hours = 0

        for date, hours in records:
            # Add "All" hours to the person's hours on that date
            all_day_hours = sum(all_hours.get(date, []))  # Sum all 'All' hours for this date
            total_hours += hours + all_day_hours  # Add 'All' hours to the person's hours

        aggregated_data[name] = total_hours

    return aggregated_data

# Function to extract total hours worked and plot the pie chart
def plot_pie_chart(aggregated_data):
    # Prepare data for pie chart
    names = list(aggregated_data.keys())
    hours = list(aggregated_data.values())

    # Create a pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(hours, labels=names, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
    plt.title("Total Hours Worked by Each Person Across All Sprints", fontsize=14, fontweight='bold')
    plt.axis('equal')  # Equal aspect ratio ensures that pie chart is a circle.
    plt.show()

def main():
    # Try reading the file line by line
    try:
        with open('sprint_log.md', 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("The file 'sprint_log.md' was not found.")
        exit()

    # Extract data from the lines of the markdown file
    data, all_hours = extract_sprint_data_from_lines(lines)

    # Aggregate the data to get total hours worked by each person
    aggregated_data = aggregate_data(data, all_hours)

    # Plot the pie chart
    plot_pie_chart(aggregated_data)

if __name__ == '__main__':
    main()
