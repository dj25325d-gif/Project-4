dataset = []
summary = {}


def flatten(data):
    """Convert a 2D list into a 1D list so calculations can be done easily."""
    flat = []
    for item in data:
        if type(item) == list:
            for x in item:
                flat.append(x)
        else:
            flat.append(item)
    return flat


def input_data():
    """Take user input and store either a 1D or 2D list in the dataset."""
    global dataset
    dataset = []

    print("1. Please enter your 1D list")
    print("2. Please enter your 2D list")

    choice = int(input("Choose option: "))

    if choice == 1:
        values = input("Enter data for a 1D array(Separated by spaces): ")
        for v in values.split():
            dataset.append(int(v))

    elif choice == 2:
        rows = int(input("Enter Rows: "))
        for i in range(rows):
            row = []
            values = input("Enter Row: ")
            for v in values.split():
                row.append(int(v))
            dataset.append(row)

    print("Data stored!")


def factorial(n):
    """Calculate factorial of a number using recursion."""
    if n == 0:
        return 1
    return n * factorial(n - 1)



def calculate_stats(data):
    """Return minimum, maximum, sum, and average of the dataset."""
    total = sum(data)
    count = len(data)

    if count == 0:
        return None

    avg = total / count
    return min(data), max(data), total, avg


def show_kwargs(**data):
    """Display summary information using keyword arguments."""
    for key in data:
        print(key, ":", data[key])



while True:

    print("\nMain Menu")
    print("1. Input Data")
    print("2. Display Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics")
    print("7. Exit")

    choice = int(input("Choice: "))

    if choice == 1:
        input_data()

    elif choice == 2:
        if not dataset:
            print("No data available. Please input data first.")
            continue

        data = flatten(dataset)

        summary = {
            "Total": len(data),
            "Min": min(data),
            "Max": max(data),
            "Sum": sum(data),
            "Average": round(sum(data)/len(data), 2)
        }

        print("\nSummary:")
        show_kwargs(**summary)

    elif choice == 3:
        n = int(input("Enter number: "))
        print("Factorial of", n, "is:", factorial(n))

    elif choice == 4:
        if not dataset:
            print("No data available. Please input data first.")
            continue

        data = flatten(dataset)
        limit = int(input("Enter a threshold Value to filter out data above this value: "))
        filtered = list(filter(lambda x: x >= limit, data))
        print("Filtered Data (Value >= 50):", filtered)

    elif choice == 5:
        if not dataset:
            print("No data available. Please input data first.")
            continue

        data = flatten(dataset)

        print("1. Sort in Ascending order")
        print("2. Sort in Descending order")

        opt = int(input("Option: "))

        if opt == 1:
            print("Sorted:", sorted(data))
        else:
            print("Sorted:", sorted(data, reverse=True))

    elif choice == 6:
        if not dataset:
            print("No data available. Please input data first.")
            continue

        data = flatten(dataset)
        stats = calculate_stats(data)

        if stats is None:
            print("Dataset is empty.")
        else:
            a, b, c, d = stats
            print("Min:", a)
            print("Max:", b)
            print("Sum:", c)
            print("Average:", round(d, 2))

    elif choice == 7:
        print("Goodbye!")
        break

    else:
        print("Invalid choice")
