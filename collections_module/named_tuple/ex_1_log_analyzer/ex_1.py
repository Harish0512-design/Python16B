# Log Data Analysis (Server / Application Logs):
from collections import namedtuple


def read_log_file(filepath: str) -> list[str]|dict:
    try:
        with open(filepath) as file:
            res = file.readlines()
            return res
    except FileNotFoundError:
        return {
            "Error": "Invalid file/File not found at the path"
        }
    
def process_log_file(list_of_logs: list[str]) -> list:
    Log = namedtuple('Log', ['timestamp', 'level', 'message'])

    structured_logs = []
    for log in list_of_logs:
        # Split by ' - ' since that's the separator in your logs
        parts = log.strip().split(' - ', 2)  # Split max 2 times to keep message intact
        if len(parts) == 3:
            timestamp, level, message = parts
            structured_logs.append(Log(timestamp, level, message))
    return structured_logs


def filter_by_log_levels(structured_logs: list, log_level: str) -> list:
    """
    Filters Logs based on the log_level
    Args:
        structured_logs: list[namedtuple], list of named tuples
        log_level: str
    returns:
        filtered_logs: list[namedtuple], list of named tuples
    """
    filtered_logs = [log for log in structured_logs if log.level == log_level]
    return filtered_logs


def count_log_levels(structured_logs: list) -> dict:
    """
    Counts the occurrences of each log level
    Args:
        structured_logs: list[namedtuple], list of named tuples
    returns:
        level_counts: dict, counts of each log level
    """
    level_counts = {}
    for log in structured_logs:
        level_counts[log.level] = level_counts.get(log.level, 0) + 1
    return level_counts


if __name__ == "__main__":
    filepath = r"collections_module\\named_tuple\\ex_1_log_analyzer\\app.log"
    logs = read_log_file(filepath)
    
    if isinstance(logs, dict):
        print(logs["Error"])
    else:
        structured_logs = process_log_file(logs)
        print("All logs:", len(structured_logs))
        
        # Filter ERROR logs
        error_logs = filter_by_log_levels(structured_logs, "ERROR")
        print("Error logs:", len(error_logs))
        print(error_logs)
        
        # Count logs by level
        level_counts = count_log_levels(structured_logs)
        print("Log level counts:", level_counts)



# output:
# All logs: 10
# Error logs: 4
# [Log(timestamp='2025-10-19 12:55:25,778', level='ERROR', message='Failed login attempt detected.'), Log(timestamp='2025-10-19 12:55:25,778', level='ERROR', message='File uploaded successfully.'), Log(timestamp='2025-10-19 12:55:25,778', level='ERROR', message='Payment processed successfully.'), Log(timestamp='2025-10-19 12:55:25,778', level='ERROR', message='User profile updated.')]
# Log level counts: {'WARNING': 3, 'ERROR': 4, 'INFO': 3}