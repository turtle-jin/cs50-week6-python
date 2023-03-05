import csv
import requests


def main():
    # Read NYTimes Covid Database
    download = requests.get(
        "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv"
    )
    decoded_content = download.content.decode("utf-8")
    file = decoded_content.splitlines()
    reader = csv.DictReader(file)

    # Construct 14 day lists of new cases for each states
    new_cases = calculate(reader)

    # Create a list to store selected states
    states = []
    print("Choose one or more states to view average COVID cases.")
    print("Press enter when done.\n")

    while True:
        state = input("State: ")
        if state in new_cases:
            states.append(state)
        if len(state) == 0:
            break

    print(f"\nSeven-Day Averages")

    # Print out 7-day averages for this week vs last week
    comparative_averages(new_cases, states)


# TODO: Create a dictionary to store 14 most recent days of new cases by state
def calculate(reader):
    new_cases = {}
    previous_cases = {}

    for row in reader:
        state = row["state"]
        cases = int(row["cases"])
        if state not in new_cases:
            new_cases[state] = []  # initialize the list
        if state not in previous_cases:
            previous_cases[state] = cases
            new_case_count = 0
        else:
            new_case_count = cases - previous_cases[state]
            new_cases[state].append(new_case_count)
            previous_cases[state] = cases  # update the previous_case counts to the current
            if len(new_cases[state]) > 14:
                new_cases[state].pop(0)
    return new_cases


# TODO: Calculate and print out seven day average for given state
def comparative_averages(new_cases, states):
    for state in states:
        first_7_days = new_cases[state][:7]
        last_7_days = new_cases[state][-7:]
        sum_last = sum(last_7_days)
        sum_first = sum(first_7_days)
        avg_last = round(sum_last / 7)
        avg_first = round(sum_first / 7)
        if avg_last > avg_first:
            try:
                percentage_increase = round(((avg_last - avg_first) / avg_first) * 100)
                print(f"{state} had a 7-day average of {avg_last} and an increase of {percentage_increase}%.")
            except ZeroDivisionError:
                print(f"{state} had a 7-day average of {avg_last}, and no percentage increase or decrease available.")
        elif avg_last < avg_first:
            try:
                percentage_decrease = round(((avg_first - avg_last) / avg_first) * 100)
                print(f"{state} had a 7-day average of {avg_last} and a decrease of {percentage_decrease}%.")
            except ZeroDivisionError:
                print(f"{state} had a 7-day average of {avg_last} and no percentage increase or decrease available.")
        else:
            print(f"{state} had a 7-day average of{avg_last}, and it stayed the same as last week's data")


main()
