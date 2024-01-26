import sys

def analyze_cat_shelter_log(log_file):
    """
    Analyzes the cat shelter log file and prints the required statistics.
    Args:
        log_file (str): The path to the cat shelter log file.

    Returns:
        None
    """
    try:
        # Open the log file for reading
        with open(log_file, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f'Cannot open "{log_file}"!')
        return

    cat_visits = 0
    other_cats = 0
    total_time_in_house = 0
    durations = []

    # Iterate through each line in the log file
    for line in lines:
        # Split the line into parts using commas as separators
        parts = line.strip().split(',')

        # Check if the line represents the end of the file
        if parts[0] == 'END':
            break

        cat_type, entry_time, exit_time = parts

        # Convert entry and exit times to integers
        entry_time = int(entry_time)
        exit_time = int(exit_time)

        # Calculate the duration of the visit
        duration = exit_time - entry_time

        if cat_type == 'OURS':
            # Count the visits by the correct cat
            cat_visits += 1
            # Track the duration for OURS cat
            durations.append(duration)
            total_time_in_house += duration
        elif cat_type == 'THEIRS': 
            # Count the visits by other cats
            other_cats += 1

    # Calculate statistics for the correct cat only
    if cat_visits > 0:
        average_duration = total_time_in_house / cat_visits
        longest_duration = max(durations)
        shortest_duration = min(durations)
    else:
        average_duration = longest_duration = shortest_duration = 0

    # Format and print the results
    print(f"$ ./cat_shelter.py {log_file}")
    print("\n Log File Analysis")
    print("="*17 )
    
    print(f"\nCat Visits: {cat_visits}")
    print(f"Other Cats: {other_cats}\n")
    print(f"Total Time in House: {format_time(total_time_in_house)}\n")
    print(f"Average Visit Length: {format_time(average_duration)}")
    print(f"Longest Visit:        {format_time(longest_duration)}")
    print(f"Shortest Visit:       {format_time(shortest_duration)}")

def format_time(minutes):
    """
    Formats the given time in minutes to a readable string.

    Args:
        minutes (int): The time in minutes.

    Returns:
        str: Formatted time string.
    """
    hours, mins = divmod(minutes, 60)
    if hours > 0:
        return f"{int(hours)} Hours, {int(mins)} Minutes"
    else:
        return f"{int(mins)} Minutes"

if __name__ == "__main__":
    # Check for the correct number of command-line arguments
    if len(sys.argv) != 2:
        print("Missing command line argument!")
    else:
        # Analyze the cat shelter log file
        analyze_cat_shelter_log(sys.argv[1])
