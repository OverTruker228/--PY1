list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]


m = 0;
a = 0;
b = len(list_numbers);
for i in range(0, len(list_numbers)-1):
    if (list_numbers[i] > m):
        m = list_numbers[i];
        a = i;

list_numbers[a], list_numbers[b-1] = list_numbers[b - 1], list_numbers[a]
print(list_numbers)
