from datetime import datetime
def get_timestamp():
    # generate timespance
    unformatted_time = datetime.now()
    formatted_time = unformatted_time.strftime("%Y%m%d%H%M%S")
    return formatted_time