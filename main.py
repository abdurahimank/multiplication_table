def multiplication_table(start, stop):
    for x in range(start, stop + 1):
        for y in range(start, stop + 1):
            print(str(x * y), end=" ")
        print()


# Should print the multiplication table of numbers from 1 to 10
multiplication_table(1, 10)
