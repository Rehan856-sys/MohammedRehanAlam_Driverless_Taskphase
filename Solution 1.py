n = int(input("Enter the number of strings: "))

strings = []

for i in range(n):
    strings.append(input("Enter string: "))

frequency = {}

for s in strings:
    for ch in s.lower():
        if ch.isalpha():
            if ch in frequency:
                frequency[ch] += 1
            else:
                frequency[ch] = 1

print(frequency)