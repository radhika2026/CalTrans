from datetime import datetime

def adjust_time_parameters(start_time, end_time):
    start_time_str = datetime.utcfromtimestamp(start_time).strftime('%m/%d/%Y %H:%M')
    end_time_str = datetime.utcfromtimestamp(end_time).strftime('%m/%d/%Y %H:%M')

    encoded_start_time_str = start_time_str.replace('/', '%2F').replace(' ', '+').replace(':', '%3A')
    encoded_end_time_str = end_time_str.replace('/', '%2F').replace(' ', '+').replace(':', '%3A')

    return encoded_start_time_str, encoded_end_time_str