# function that will print the map
def mapping():
    # taking no. of lines from the user
    N = int(input("Enter the no. of lines you want to insert: "))

    # list for storing the intial map
    data = []

    print("Enter the intial map")
    for i in range(N):
        data.append(input())
        print(data)
    print("\nFinal map")
    # variable that will count no. of stars
    k = 0
    # iterating in the data
    for i in data:
        # if empty line encountered means new
        # mapping now
        if i == "":
            print()
            k = 0
            continue

        # counting and printing the results
        c = i.count("*")
        print("." * (len(i) - c - k), end="")
        print("*" * c, end="")
        print("." * k)
        k += c

mapping()