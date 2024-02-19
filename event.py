






# import os

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

#     with open(output_path, 'w') as output_file:
#         output_file.write("SubscriptionId,Timestamp,LogLevel,Tag\n")
#         current_subscription_id = ""
#         current_timestamp = ""
#         current_log_levels = []
#         current_tags = []
#         for file_name in files:
#             file_path = os.path.join(input_path, file_name)
#             with open(file_path, 'r') as input_file:
#                 for line in input_file:
#                     event_id, timestamp, actions = separate_event(line.strip())
#                     if event_id is not None:
#                         if current_subscription_id != event_id:
#                             if current_subscription_id:
#                                 output_file.write(f"{current_subscription_id},{current_timestamp},")
#                                 output_file.write(",".join(current_log_levels) + ",")
#                                 output_file.write(",".join(current_tags) + "\n")
#                             current_subscription_id = event_id
#                             current_timestamp = timestamp
#                             current_log_levels = []
#                             current_tags = []
#                         else:
#                             current_timestamp = timestamp
#                         for action in actions:
#                             components = action.split(",")
#                             if len(components) >= 2:
#                                 current_log_levels.append(components[0])
#                                 current_tags.append(components[1])
#         if current_subscription_id:
#             output_file.write(f"{current_subscription_id},{current_timestamp},")
#             output_file.write(",".join(current_log_levels) + ",")
#             output_file.write(",".join(current_tags) + "\n")

# # Example usage:
# input_path = r"C:\Users\ASUS\OneDrive\Desktop\angadiappevents"
# output_path = "output.csv"
# process_files(input_path, output_path)













import os

def separate_event(event):
    colon_index = event.find(':')

    if colon_index != -1:
        event_id = event[:colon_index]
        event_data = event[colon_index + 1:]

        parts = event_data.split("[", 1)

        if len(parts) == 2:
            timestamp, actions_data = parts
            actions = actions_data.rstrip("]").split(",")
            return event_id, timestamp, actions
        else:
            return None, None, None
    else:
        return None, None, None

def process_files(input_path, output_path):
    files = os.listdir(input_path)

    with open(output_path, 'w') as output_file:
        output_file.write("SubscriptionId,Timestamp,LogLevel,Tag\n")
        for file_name in files:
            file_path = os.path.join(input_path, file_name)
            with open(file_path, 'r') as input_file:
                current_subscription_id = ""
                for line in input_file:
                    event_id, timestamp, actions = separate_event(line.strip())
                    if event_id is not None:
                        if current_subscription_id != event_id:
                            if current_subscription_id:
                                for timestamp, log_level, tag in zip(timestamps, log_levels, tags):
                                    output_file.write(f"{current_subscription_id},{timestamp},{log_level},{tag}\n")
                            current_subscription_id = event_id
                            timestamps = []
                            log_levels = []
                            tags = []
                        timestamps.extend([timestamp] * (len(actions) // 2))
                        log_levels.extend(actions[::2])
                        tags.extend(actions[1::2])
                if current_subscription_id:
                    for timestamp, log_level, tag in zip(timestamps, log_levels, tags):
                        output_file.write(f"{current_subscription_id},{timestamp},{log_level},{tag}\n")

# Example usage:
input_path = r"C:\Users\ASUS\OneDrive\Desktop\angadiappevents"
output_path = "output.csv"
process_files(input_path, output_path)
