import cleaner
import stats
import plots


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

    # open file and read it into the data list
    with open(file, "r") as f:
        for line in f:
            data.append(line)


    # clean the data and remove invalid entries
    cleaned_list, removed_values = cleaner.clean_heartrate_data(data)

    # calculate the average, median, and range
    hr_avg = stats.average(cleaned_list)

    hr_med = stats.median(cleaned_list)

    hr_range = stats.range(cleaned_list)

    hr_roll_avg = stats.rolling_avg(cleaned_list, k = 6)

    hr_variance = stats.variance(cleaned_list)

    print("\n" + "="*40)
    print(f"Heart Rate Report: {file}")
    print("="*40)

    # print data quality measure to the console
    print(f"Data Quality: Removed {len(removed_values)} invalid entries.")

    # print out descriptive statistics to the console
    print(f"Average Heartrate: {hr_avg:}")
    print(f"Median Heartrate:  {hr_med}")
    print(f"Heartrate Range:  {hr_range}")
    print(f"Rolling Averages: {hr_roll_avg[:5]}")
    print(f"Heartrate variance: {hr_variance}")

    # generate plots and save to folder
    plots.plts(cleaned_list, file, hr_avg, hr_variance)



if __name__ == "__main__":
    run("data/phase0.txt")
    run("data/phase1.txt")
    run("data/phase2.txt")
    run("data/phase3.txt")
