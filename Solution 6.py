def find_position(arr, num):

    low = 0
    high = len(arr)

    while low < high:

        mid = (low + high) // 2

        if arr[mid] < num:
            low = mid + 1
        else:
            high = mid

    return low


n = int(input("Enter n: "))

hash_table = [[] for i in range(10)]

for i in range(n):

    num = int(input("Enter number: "))

    index = num % 10

    bucket = hash_table[index]

    position = find_position(bucket, num)

    bucket.insert(position, num)


print("Hash table:")

for i in range(10):
    print(i, ":", hash_table[i])