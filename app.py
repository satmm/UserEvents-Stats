# import streamlit as st
# import pandas as pd
# from io import StringIO

# def separate_event(event):
#     # Function to separate event components
#     colon_index = event.find(':')

#     if colon_index != -1:
#         event_id = event[:colon_index]
#         event_data = event[colon_index + 1:]

#         parts = event_data.split("[", 1)

#         if len(parts) == 2:
#             timestamp, actions_data = parts
#             actions_data = actions_data.rstrip("]").split(",")
#             if len(actions_data) >= 2:
#                 log_level = actions_data[0].split(":")[-1]
#                 tag = actions_data[1].strip()
#                 return event_id.strip(), timestamp.strip(), log_level.strip(), tag.strip()
#             else:
#                 return None, None, None, None
#         else:
#             return None, None, None, None
#     else:
#         return None, None, None, None

# def process_data():
#     # Sample data
#     sample_data = """
#     SubscriptionId\tTimestamp\tLogLevel\tTag
#     7e68195f-84a1-4b5c-b20c-26bfadb41b1c\t1.70733E+12\t0\tN_REGUSER_NO
#     7e68195f-84a1-4b5c-b20c-26bfadb41b1c\t1.70733E+12\t0\tB_BASKET_6
#     7e68195f-84a1-4b5c-b20c-26bfadb41b1c\t1.70733E+12\t0\tS_PRODUCTS_ADD
#     7e68195f-84a1-4b5c-b20c-26bfadb41b1c\t1.70733E+12\t0\tLASTEVENTPOST
#     """

#     # Read sample data into DataFrame
#     df = pd.read_csv(StringIO(sample_data), delimiter="\t")

#     return df

# def main():
#     st.title("Event Capture App")

#     # Process data
#     df = process_data()

#     # Display DataFrame
#     st.write(df)

# if __name__ == "__main__":
#     main()









import os
import streamlit as st

def separate_event(event):
    # Function to separate event components
    colon_index = event.find(':')

    if colon_index != -1:
        event_id = event[:colon_index]
        event_data = event[colon_index + 1:]

        parts = event_data.split("[", 1)

        if len(parts) == 2:
            timestamp, actions_data = parts
            actions_data = actions_data.rstrip("]").split(",")
            if len(actions_data) >= 2:
                log_level = actions_data[0].split(":")[-1]
                tag = actions_data[1].strip()
                return event_id.strip(), timestamp.strip(), log_level.strip(), tag.strip()
            else:
                return None, None, None, None
        else:
            return None, None, None, None
    else:
        return None, None, None, None

def process_files(input_path):
    # Function to process input files and generate output CSV
    files = os.listdir(input_path)
    output_data = []

    for file_name in files:
        file_path = os.path.join(input_path, file_name)
        with open(file_path, 'r') as input_file:
            for line in input_file:
                event_id, timestamp, log_level, tag = separate_event(line.strip())
                if event_id is not None:
                    output_data.append([event_id, timestamp, log_level, tag])

    return output_data

# Example usage of process_files
input_path = r"C:\Users\ASUS\OneDrive\Desktop\angadiappevents"
output_data = process_files(input_path)



# Display the output data using Streamlit
st.write("## Event Data")
st.write("SubscriptionId | Timestamp | LogLevel | Tag")
st.write("--- | --- | --- | ---")
for event in output_data:
    st.write(f"{event[0]} | {event[1]} | {event[2]} | {event[3]}")