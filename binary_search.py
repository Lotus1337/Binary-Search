def binary_search(data, target, low, high):

    if high >= low:
        midpoint = (high + low) // 2

        if data[midpoint] == target:
            return midpoint

        elif data[midpoint] > target:
            return binary_search(data, target, low, midpoint - 1)

        else:
            return binary_search(data, target, midpoint + 1, high)

    else:
        return -1

data = [int(x) for x in input("Enter your dataset: ").split(",")]

target = int(input("Enter your target: "))

result = binary_search(data, target, 0, len(data) - 1)

if result != -1:
    print("Target is at", result)

else:
    print("Target is not within the dataset")

