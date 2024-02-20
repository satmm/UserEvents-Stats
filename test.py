

import os
import re
import pandas as pd

def process_event(event):
    # Regex pattern to extract data
    pattern = r'(?P<subscriptionId>[^:]+):\[(?P<timeStamp>\d+):\[(?P<logLevel>[^,]+),(?P<tag>[^\]]+)\],?'

    # Find all matches in the event
    matches = re.findall(pattern, event)
    return matches

def process_files(input_directory):
    # Function to process input files and generate output CSV
    data = []

    # Iterate through each file in the directory
    for file_name in os.listdir(input_directory):
        file_path = os.path.join(input_directory, file_name)
        if os.path.isfile(file_path) and file_name.endswith('.log'):
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    matches = process_event(line.strip())
                    for match in matches:
                        data.append(match)

    # Convert data to DataFrame
    df = pd.DataFrame(data, columns=['SubscriptionId', 'Timestamp', 'LogLevel', 'Tag'])

    # Specify output file path in the directory C:\Users\ASUS\OneDrive\Desktop\Event Capture
    output_path = os.path.join("C:\\Users\\ASUS\\OneDrive\\Desktop\\Event Capture", "output.csv")
    
    # Write DataFrame to CSV
    df.to_csv(output_path, index=False)
    print(f"Output saved to {output_path}")

# Input directory path
input_directory = r"C:\Users\ASUS\OneDrive\Desktop\angadiappevents"

# Process files in the specified directory
process_files(input_directory)
