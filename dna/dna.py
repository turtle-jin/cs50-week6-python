import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit("Usage: incorrect number of arguments")

    # TODO: Read database file into a variable
    database = []
    with open(sys.argv[1]) as database_file:
        database_reader = csv.DictReader(database_file)
        for data in database_reader:
            database.append(data)

    # print(f"database is: {database}")
    list_of_keys = database[0].keys()
    STR_list = []
    for keys in list_of_keys:
        STR_list.append(keys)
    del STR_list[0]
    # print(f"STR list is {STR_list}")

    # TODO: Read DNA sequence file into a variable

    with open(sys.argv[2]) as sequence_file:
        sequence = sequence_file.read()
    # print(sequence)

    # TODO: Find longest match of each STR in DNA sequence
    matches = {}
    for STR in STR_list:
        matches[STR] = longest_match(sequence, STR)
    # print(f"matches dict: {matches}")

    # TODO: Check database for matching profiles

    target = "No match"
    first_STR = STR_list[0]
    sum_matches_values = sum(list(matches.values()))
    for i in range(len(database)):
        if int(database[i][first_STR]) == matches[first_STR]:  # check if the first STR matches
            sub_dict = database[i]  # if matches, then search only in that dict
            values_list = list(sub_dict.values())  # grab all the values in the sub dict and put them in a list
            del values_list[0]  # get rid of the first element in the list since it's a name
            int_list = [int(j) for j in values_list]  # convert all the strings in the list into int
            sum_of_list = sum(int_list)  # find the sum of the list

            # print(sub_dict)
            # print(sum_of_list)

            if sum_of_list == sum_matches_values:  # when sum of the list matches the STR values in matches
                target = database[i]['name']
                break

    # print(sum_matches_values)
    print(target)


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
