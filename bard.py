

# # # # import os

# # # # def separate_event(event):
# # # #     parts = event.split(":")
# # # #     if len(parts) >= 2:
# # # #         subscription_id = parts[0]
# # # #         actions_data = ":".join(parts[1:])
# # # #         actions = actions_data.split(",")
# # # #         timestamp = ""
# # # #         log_level = ""
# # # #         tag = ""
# # # #         if actions:
# # # #             timestamp = actions[0].split("[")[0]
# # # #             log_level = actions[0].split("[")[1]
# # # #             tag = actions[-1].split("]")[0]
# # # #         return subscription_id, timestamp, log_level, tag
# # # #     else:
# # # #         return None, None, None, None


# # # # def process_files(input_path, output_path):
# # # #     files = os.listdir(input_path)

# # # #     with open(output_path, 'w', newline='') as output_file:
# # # #         output_file.write("SubscriptionId,Timestamp,LogLevel,Tag\n")
# # # #         for file_name in files:
# # # #             file_path = os.path.join(input_path, file_name)
# # # #             with open(file_path, 'r') as input_file:
# # # #                 for line in input_file:
# # # #                     event_id, timestamp, actions = separate_event(line.strip())
# # # #                     if event_id is not None:
# # # #                         for action in actions:
# # # #                             components = action.split(",")
# # # #                             if len(components) >= 2:
# # # #                                 log_level = components[0].strip()
# # # #                                 tag = components[1].strip()
# # # #                                 output_file.write(f"{event_id},{timestamp},{log_level},{tag}\n")

# # # # # Example usage:
# # # # input_path = r"C:\Users\ASUS\OneDrive\Desktop\angadiappevents"
# # # # output_path = "output5.csv"
# # # # process_files(input_path, output_path)












# # import os
# # import csv

# # def parse_event(line):
# #     parts = line.strip().split(':[')
# #     subscription_id = parts[0].strip()
# #     timestamps_logs_tags = parts[1].strip(']').split('],[')
# #     timestamps = []
# #     logs = []
# #     tags = []
# #     for tlt in timestamps_logs_tags:
# #         tlt_parts = tlt.strip('[]').split(',')
# #         timestamp = int(tlt_parts[0], 16)
# #         log_level = int(tlt_parts[1])
# #         tag = tlt_parts[2].strip('[]')
# #         timestamps.append(timestamp)
# #         logs.append(log_level)
# #         tags.append(tag)
# #     return subscription_id, timestamps, logs, tags

# # def process_files(input_path):
# #     with open('output4.csv', 'w', newline='') as csvfile:
# #         fieldnames = ['subscription_id', 'timestamp', 'log_level', 'tag']
# #         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
# #         writer.writeheader()
# #         for file_name in os.listdir(input_path):
# #             file_path = os.path.join(input_path, file_name)
# #             if os.path.isfile(file_path):
# #                 print(f"Processing file: {file_path}")
# #                 with open(file_path, "r") as file:
# #                     for line in file:
# #                         subscription_id, timestamps, logs, tags = parse_event(line)
# #                         for timestamp, log_level, tag in zip(timestamps, logs, tags):
# #                             writer.writerow({'subscription_id': subscription_id, 'timestamp': timestamp, 'log_level': log_level, 'tag': ''.join(tag)})

# # input_path =  r"C:\Users\ASUS\OneDrive\Desktop\angadiappevents"
# # process_files(input_path)



# import os
# import csv

# def separate_event(event):
#     colon_index = event.find(':')

#     if colon_index != -1:
#         event_id = event[:colon_index]
#         event_data = event[colon_index + 1:]

#         parts = event_data.split("[", 1)

#         if len(parts) == 2:
#             timestamp, actions_data = parts
#             actions = actions_data.rstrip("]").split(",")
#             return event_id, timestamp, actions
#         else:
#             return None, None, None
#     else:
#         return None, None, None

# def process_files(input_path, output_path):
#     files = os.listdir(input_path)

#     with open(output_path, 'w', newline='') as output_file:
#         writer = csv.writer(output_file)
#         writer.writerow(["SubscriptionId", "Timestamp", "LogLevel", "Tag"])
#         for file_name in files:
#             file_path = os.path.join(input_path, file_name)
#             with open(file_path, 'r') as input_file:
#                 current_subscription_id = ""
#                 for line in input_file:
#                     event_id, timestamp, actions = separate_event(line.strip())
#                     if event_id is not None:
#                         if current_subscription_id != event_id:
#                             if current_subscription_id:
#                                 for timestamp, log_level, tag in zip(timestamps, log_levels, tags):
#                                     writer.writerow([current_subscription_id, timestamp, log_level, tag])
#                             current_subscription_id = event_id
#                             timestamps = []
#                             log_levels = []
#                             tags = []
#                         timestamps.extend([timestamp] * (len(actions) // 2))
#                         log_levels.extend(actions[::2])
#                         tags.extend(actions[1::2])
#                 if current_subscription_id:
#                     for timestamp, log_level, tag in zip(timestamps, log_levels, tags):
#                         writer.writerow([current_subscription_id, timestamp, log_level, tag])

# # Example usage:
# input_path = r"C:\Users\ASUS\OneDrive\Desktop\angadiappevents"
# output_path = "output5.csv"
# process_files(input_path, output_path)






# import os

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

# def process_files(input_path, output_path):
#     # Function to process input files and generate output CSV
#     files = os.listdir(input_path)

#     with open(output_path, 'w') as output_file:
#         output_file.write("SubscriptionId, Timestamp, LogLevel, Tag\n")
#         event_id, timestamp, log_level, tag = None, None, None, None
#         for file_name in files:
#             file_path = os.path.join(input_path, file_name)
#             with open(file_path, 'r') as input_file:
#                 for line in input_file:
#                     new_event_id, new_timestamp, new_log_level, new_tag = separate_event(line.strip())
#                     if new_event_id is not None:
#                         if event_id is not None:
#                             output_file.write(f"{event_id}, {timestamp}, {log_level}, {tag}\n")
#                         event_id, timestamp, log_level, tag = new_event_id, new_timestamp, new_log_level, new_tag
#                     else:
#                         if event_id is not None:
#                             output_file.write(f"{event_id}, {timestamp}, {log_level}, {tag}\n")
#                         event_id, timestamp, log_level, tag = None, None, None, None

# # Example usage:
# input_path = r"C:\Users\ASUS\OneDrive\Desktop\Event Capture"
# output_path = "output9.csv"
# process_files(input_path, output_path)





import os
import csv

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


def process_files(input_path, output_path):
    # Function to process input files and generate output CSV
    files = os.listdir(input_path)

    with open(output_path, 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(["EventID", "Timestamp", "LogLevel", "Tag"])
        
        for file_name in files:
            file_path = os.path.join(input_path, file_name)
            with open(file_path, 'r') as input_file:
                for line in input_file:
                    event_id, timestamp, log_level, tag = separate_event(line.strip())
                    if event_id is not None:
                        writer.writerow([event_id, timestamp, log_level, tag])

# Example usage:
# Example usage:
input_path = r"C:\Users\ASUS\OneDrive\Desktop\angadiappevents"
output_path = "output12.csv"
process_files(input_path, output_path)

