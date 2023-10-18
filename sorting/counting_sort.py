def counting_sort(arr):
    n = len(arr)
    M = max(arr)

    count_arr = [0] * (M+1)

    for i in arr:
        count_arr[i] += 1

    for i in range(1, M+1):
        count_arr[i] += count_arr[i - 1]

    output_arr = [0] * n

    for i in range(n - 1, -1, -1):
        output_arr[count_arr[arr[i]] - 1] = arr[i]
        count_arr[arr[i]] -= 1

    return output_arr

arr = [4, 3, 12, 1, 5, 5, 3, 9]

arr = counting_sort(arr)

print(arr)

