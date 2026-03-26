def average(data: list) -> float:
    """
    Calculate average of a list of integers using a for-loop. Assumes data is clean.
    """
    if not data:
        return 0.0

    total = 0
    for hr in data:
        
        total += hr

    average = round( total / len(data), 2)

    return average

def median(data: list) -> float:
    """
    """
    if not data:
        return 0.0
    
    sorted_data = sorted(data)
    
    if len(sorted_data) % 2 != 0:
        mid_index = len(sorted_data) // 2
        med = sorted_data[mid_index]
        return med
    else:
        r_index = len(sorted_data) // 2
        l_index = (len(sorted_data) // 2) - 1
        med = (sorted_data[r_index] + sorted_data[l_index]) / 2
        return round(med, 2)


def range(data: list) -> float:
    """
    """
    if not data:
        return 0.0

    max_val = data[0]
    min_val = data[0]
    
    for hr in data:
        if hr >= max_val:
            max_val = hr
        if hr <= min_val:
            min_val = hr
        
    data_range = max_val - min_val

    return data_range


def rolling_avg(data: list, k: int) -> list:
    """
    Calculate rolling average for heart rates over a specified window of time.
    """
    if not data:
        return []
    
    new_data = []

    # for i in range(len(data)):
    for i, hr in enumerate(data): # changed from 'in range' to "i, hr in enumerate" to avoid shadowing conflict
        window = data[ i : i + k]

        window_avg = average(window)
        rounded_avg = round(window_avg, 2)

        new_data.append(rounded_avg)
    return new_data

def run(file: str):
    """
    Process heart rate data from the a file by cleaning and
    calculating summary statistics. Print out final values.

    Args:
        filename (str): The path to the data file (e.g., 'data/phase0.txt').

    Returns:
        float, float, float: You will return the average, median, and range.
    """
    data = []

    # open file using file I/O and read it into the `data` list
    with open(file, "r") as f:
        for line in f:
            data.append(line)


    # Use `clean_heartrate_data` to clean the data and remove invalid entries

    cleaned_list, removed_values = clean_heartrate_data(data)

    # calculate the average, median, and range of this file using the functions you've wrote
    hr_avg = average(cleaned_list)

    hr_med = median(cleaned_list)

    hr_range = range(cleaned_list)

    hr_roll_avg = rolling_avg(cleaned_list, k = 6)
