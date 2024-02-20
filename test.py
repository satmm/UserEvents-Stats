


import os
import re
import pandas as pd

def process_event(event):
  
    pattern = r'(?P<subscriptionId>[^:]+):\[(?P<timeStamp>\d+):\[(?P<logLevel>[^,]+),(?P<tag>[^\]]+)\],?'

  
    matches = re.findall(pattern, event)
    return matches

def process_files(input_directory):
   
    data = []

    for file_name in os.listdir(input_directory):
        file_path = os.path.join(input_directory, file_name)
        if os.path.isfile(file_path) and file_name.endswith('.log'):
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    matches = process_event(line.strip())
                    for match in matches:
                        data.append(match)

    
    df = pd.DataFrame(data, columns=['SubscriptionId', 'Timestamp', 'LogLevel', 'Tag'])

   
    output_path = os.path.join("C:\\Users\\ASUS\\OneDrive\\Desktop\\Event Capture", "output.csv")
    
   
    df.to_csv(output_path, index=False)
    print(f"Output saved to {output_path}")


input_directory = r"C:\Users\ASUS\OneDrive\Desktop\angadiappevents"


process_files(input_directory)












