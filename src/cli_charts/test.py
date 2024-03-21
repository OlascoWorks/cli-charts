# values = [[2,3], [5,4], [3,1], [7,4], [2,6], [1,4]]

# # coords = {coord[1]:[coord[0]] for coord in values if not coords[coord[1]] [coords[coord[1]], coord[0]]}
# coords =  {}
# for value in values:
#     if value[1] not in coords.keys():  coords[value[1]] = value[0]
#     else:
#         if type(coords[value[1]]) == list:  coords[value[1]].append(value[0])
#         else:  coords[value[1]] = [coords[value[1]],value[0]]

# print(coords)

# import math

# def round_to_tens(num):
#     return math.ceil(num / 10) * 10

# print(round_to_tens(45))  # Output: 50
# print(round_to_tens(22))  # Output: 30
# print(round_to_tens(91))  # Output: 100
# print(round_to_tens(74))  # Output: 80


import math
class CHART:
    def __init__(self, granular=False) -> None:
        self.granular = granular

    def draw_bar(self, values:list, barWidth=5, space=3):
        for value in values:
            if type(value) != list:  raise TypeError("Values must be a list of lists")
            if type(value[0]) != str or type(value[1]) != int:  raise TypeError("Coordinates must be a list of a string and an integer(in order)")

            for iter, coord in enumerate(value):
                if type(coord) == int and self.granular == True:  value[iter] = value[iter] +1 if value[iter] % 2 != 0 else value[iter]

        yMax = max([cord[1] for cord in values])
        xMax = (barWidth + space) *len(values)
        yTop = math.ceil(yMax / 10) * 10
        xTop = math.ceil(xMax / 10) * 10
        labelWidth = len(str(yMax)) +1
        step = 2 if self.granular == True else 1
        coordinates = {}
        bar_list = []
        chart = f"""{' ' *labelWidth}.\n{' ' *labelWidth}.\n{' ' *labelWidth}.\n"""

        next_coord = space
        coord_list = []
        for value in values:
            print(coordinates)
            if value[1] not in coordinates.keys():  coordinates[value[1]] = [value[0], next_coord]
            else:
                if type(coordinates[value[1]]) == list:  coordinates[value[1]].append([coordinates[value[1]], value[0]])
                else:  coordinates[value[1]] = [coordinates[value[1]],value[0]]

                # coordinates[value[1]] = sorted(coordinates[value[1]][1:])
                # coord_list.append(next_coord)

            next_coord = next_coord + barWidth + space

        for iter in range(0, yTop+1, step):
            pos = yTop - iter
            if pos % 10 == 0 and pos != 0:  chart += str(pos) + " +"
            elif pos == 0:
                chart += ' ' + str(pos) + " +"
                for n in range(int(xTop/10)):
                    if n*10 !=( xTop -10):  chart += "---------+"
                    else:
                        chart += "---------+---\n"
                        for n in range(int(xTop/10)):
                            if n == 0:  chart += f"{' ' *labelWidth}         {(n*10) +10}"
                            else:  chart += f"        {(n*10) +10}"
            else:  chart += f"{' ' *labelWidth}."

            if pos in coordinates.keys():
                bar_list.append(pos)
                bar_list = sorted(bar_list)
                
            plot = ''
            for k, bar in enumerate(bar_list):
                if k == 0:  plot += " "*(coordinates[pos][-1] - 1) + "*"*barWidth
                else:  plot += " "*((coordinates[pos][-1] -len(plot)) -1) + "*"*barWidth
                if k == len(coordinates[pos]) -1:  plot += "\n"

            chart += plot
            
            #     if type(coordinates[pos]) == list:
            #         coords = coordinates[pos]
            #         plot = ''
            #         for k, n in enumerate(coords):
            #             if k == 0:  plot += " "*(coordinates[pos][k] - 1) + "*"
            #             else:  plot += " "*((coordinates[pos][k] -len(plot)) -1) + "*"
            #             if k == len(coords) -1:  plot += "\n"

            #         chart += plot
            #     else:
            #         chart += " "*(coordinates[pos] -1) + "*\n"
            # else:
            #     chart += f'{' ' *labelWidth}\n'

        print(chart)

chart = CHART()
chart.draw_bar([['A', 20], ['B', 40], ['C', 10], ['D', 20], ['E', 100]])