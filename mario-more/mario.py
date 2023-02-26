def get_height():
    while True:
        try:
            n = int(input("Height: "))
            if n < 1 or n > 8:
                print("Height must be between 1 and 8.")
            else:
                return n
        except ValueError:
            print("Not an integer.")


def main():
    height = get_height()
    for i in range(height):
        for space_1 in range(height - 1, i, -1):
            print(" ", end="")
        for block_1 in range(0, i + 1, 1):
            print("#", end="")
        print("  ", end="")
        for block_2 in range(0, i + 1, 1):
            print("#", end="")
        print()


main()