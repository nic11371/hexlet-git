def binary_sum(num_1, num_2):
    binary_1 = int(num_1, 2)
    binary_2 = int(num_2, 2)

    return bin(binary_1 + binary_2)[2:]


print(binary_sum('1101', '101'))
