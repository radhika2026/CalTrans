from datetime import datetime

def adjust_time_parameters(timestamp):
            if isinstance(timestamp, int):  # Check if timestamp is Unix timestamp
                time_str = datetime.utcfromtimestamp(timestamp).strftime('%m/%d/%Y %H:%M')
            else:  
                time_str = timestamp
            return time_str.replace('/', '%2F').replace(' ', '+').replace(':', '%3A')