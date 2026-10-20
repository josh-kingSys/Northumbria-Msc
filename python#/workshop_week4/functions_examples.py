def multiply_numbers_min_to_max(min,max,multiplier):
    list = []
    for i in range(min, max):
        list.append(i * multiplier)
            
    return list

output2 = multiply_numbers_min_to_max(50, 55, 55)

print(output2)