class Search:
    def binary_search(self, arr, target):

        low = 0
        high = len(arr) - 1

        while low <= high:

            mid = (low + high) // 2

            if arr[mid] == target:
                return mid

            elif arr[mid] < target:
                low = mid + 1

            else:
                high = mid - 1

        return -1


class Sort:
    def selection_sort(self, arr):

        n = len(arr)

        for i in range(n):
            min_index = i

            for j in range(i + 1, n):
                if arr[j] < arr[min_index]:
                    min_index = j

            arr[i], arr[min_index] = arr[min_index], arr[i]

        return arr


n = int(input("Enter n: "))

words = []

for i in range(n):
    words.append(input("Enter string: "))

sorter = Sort()
searcher = Search()

sorter.selection_sort(words)

print("Sorted list:", words)

target = input("Enter string to search: ")

result = searcher.binary_search(words, target)

if result != -1:
    print("String found at index", result)
else:
    print("String not found")