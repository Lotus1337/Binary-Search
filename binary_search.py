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
        return - 1

data = [745, 1534, 2969, 4144, 4328, 5276, 5985, 6713, 6895, 7642]

target = 2969

result = binary_search(data, target, 0, len(data) - 1)

if result != -1:
    print("Target is at", str(result))
else:
    print("Target is not present in data")
