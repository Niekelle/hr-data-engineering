def clean_heartrate_data(data: list) -> tuple:
    """
    Clean raw heart-rate data by removing malformed or impossible values.
    """
    cleaned_list = []
    removed_values = []

    for hr in data:
        stripped_hr = hr.strip()

        if stripped_hr.isdigit() and 40 <= int(stripped_hr) <= 190:
            cleaned_list.append(int(stripped_hr))
        else:
            removed_values.append(stripped_hr)

    return cleaned_list, removed_values