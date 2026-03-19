def clean_heartrate_data(data: list) -> tuple:
    """
    Clean raw heart-rate data by removing malformed or impossible values.
    """
    cleaned_list = []
    removed_values = []

    for hr in data:
        if hr.isdigit() and 30 <= int(hr) <= 250:
            cleaned_list.append(int(hr))
        else:
            removed_values.append(hr)

    return cleaned_list, removed_values

def average(data: list) -> float:
    """
    Calculate average of a list of integers using a for-loop. Assumes data is clean.
    """
    if not data:
        return 0.0

    total = 0
    for hr in data:
        
        total += hr

    average =  total / len(data)

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
        return med


def range(data: list) -> float:
    """
    """
    if not data:
        return 0.0

    data_range = max(data) - min(data)

    return data_range


def rolling_avg(data: list, k: int) -> float:
    """
    CHALLENGE FUNCTION (Optional)
    """
    pass


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
            data.append(line.strip())


    # Use `clean_heartrate_data` to clean the data and remove invalid entries

    cleaned_list, removed_values = clean_heartrate_data(data)

    # calculate the average, median, and range of this file using the functions you've wrote
    

    # print out your data quality measure to the console
    ...

    # print out your descriptive statistics to the console
    ...


if __name__ == "__main__":
    run("data/phase0.txt")
    run("data/phase1.txt")
    run("data/phase2.txt")
    run("data/phase3.txt")
