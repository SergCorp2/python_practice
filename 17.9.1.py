
sequence = input('введите последовательность чисел через пробел:')
sequence_mod = [int(a) for a in sequence.split()]
if (' ' not in (sequence)):
    raise ValueError("Введены некорректные данные! Введите последовательность чисел через пробел!")

num = int(input('введите число:'))
if max(sequence_mod, key=lambda i: int(i)) >= num >= min(sequence_mod, key=lambda  i: int(i)):
    sequence_mod.append(num)
else:
    raise ValueError("Введены некорректные данные!")

for i in range(len(sequence_mod)):
    for j in range(len(sequence_mod) - i - 1):
        if sequence_mod[j] > sequence_mod[j + 1]:
            sequence_mod[j], sequence_mod[j + 1] = sequence_mod[j + 1], sequence_mod[j]

print('отсортированная последовательность:', sequence_mod)


def binary_search(sequence_mod, num, left, right):
    if left > right:
        return False

    middle = (left + right) // 2
    if sequence_mod[middle] == num:
        return middle
    elif num < sequence_mod[middle]:
        return binary_search(sequence_mod, num, left, middle - 1)
    else:
        return binary_search(sequence_mod, num, middle + 1, right)

print('индекс искомых чисел', binary_search(sequence_mod, num, 0, len(sequence_mod) - 1) - 1,
          #binary_search(sequence_mod, num, 0, len(sequence_mod) - 1)) or
          binary_search(sequence_mod, num, 0, len(sequence_mod) - 1) + 1)


#print(binary_search(sequence_mod, num, 0, len(sequence_mod) - 1))