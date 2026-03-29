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
    calculate rolling average for heart rates over a specified window of time.

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

def variance(data: list) -> float:
    """
    """
    xbar = sum(data) / len(data)
    
    var = sum((x-xbar)**2 for x in data) / (len(data) - 1)

    return round(var, 2)
    

