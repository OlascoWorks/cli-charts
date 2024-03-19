# values = [[2,3], [5,4], [3,1], [7,4], [2,6], [1,4]]

# # coords = {coord[1]:[coord[0]] for coord in values if not coords[coord[1]] [coords[coord[1]], coord[0]]}
# coords =  {}
# for value in values:
#     if value[1] not in coords.keys():  coords[value[1]] = value[0]
#     else:
#         if type(coords[value[1]]) == list:  coords[value[1]].append(value[0])
#         else:  coords[value[1]] = [coords[value[1]],value[0]]

# print(coords)

import math

def round_to_tens(num):
    return math.ceil(num / 10) * 10

print(round_to_tens(45))  # Output: 50
print(round_to_tens(22))  # Output: 30
print(round_to_tens(91))  # Output: 100
print(round_to_tens(74))  # Output: 80