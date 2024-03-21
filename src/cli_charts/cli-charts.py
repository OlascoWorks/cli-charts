import math

class CHART:
    def __init__(self, granular=False) -> None:
        self.granular = granular

    def plot_graph(self, values:list):
        for value in values:
            if type(value) != list:  raise TypeError("Values must be a list of lists")

            for iter, coord in enumerate(value):
                if type(coord) != int and type(coord) != float:  raise TypeError("coordinates must be a list of lists of numbers")
                value[iter] = round(coord)
                if self.granular == True:  value[iter] = value[iter] +1 if value[iter] % 2 != 0 else value[iter]

        yMax = max([cord[1] for cord in values])
        xMax = max([cord[0] for cord in values])
        yTop = math.ceil(yMax / 10) * 10
        xTop = math.ceil(xMax / 10) * 10
        labelWidth = len(str(yMax)) +1
        step = 2 if self.granular == True else 1
        coordinates = {}
        graph = f"""{' ' *labelWidth}.\n{' ' *labelWidth}.\n{' ' *labelWidth}.\n"""

        for value in values:
            if value[1] not in coordinates.keys():  coordinates[value[1]] = value[0]
            else:
                if type(coordinates[value[1]]) == list:  coordinates[value[1]].append(value[0])
                else:  coordinates[value[1]] = [coordinates[value[1]],value[0]]

                coordinates[value[1]] = sorted(coordinates[value[1]])

        for iter in range(0, yTop+1, step):
            pos = yTop - iter
            if pos % 10 == 0 and pos != 0:  graph += str(pos) + " +"
            elif pos == 0:
                graph += ' ' + str(pos) + " +"
                for n in range(int(xTop/10)):
                    if n*10 !=( xTop -10):  graph += "---------+"
                    else:
                        graph += "---------+---\n"
                        for n in range(int(xTop/10)):
                            if n == 0:  graph += f"{' ' *labelWidth}         {(n*10) +10}"
                            else:  graph += f"        {(n*10) +10}"
            else:  graph += f"{' ' *labelWidth}."

            if pos in coordinates.keys():
                if type(coordinates[pos]) == list:
                    coords = coordinates[pos]
                    plot = ''
                    for k, n in enumerate(coords):
                        if k == 0:  plot += " "*(coords[k] - 1) + "*"
                        else:  plot += " "*((coords[k] -len(plot)) -1) + "*"
                        if k == len(coords) -1:  plot += "\n"

                    graph += plot
                else:
                    graph += " "*(coordinates[pos] -1) + "*\n"
            else:
                graph += f'{' ' *labelWidth}\n'

        print(graph)

    # def draw_bar(elf, values:list, barWidth=5):

    def __str__(self) -> str:
        return ""

    def __repr__(self) -> str:
        return self.__str__
    

chart1 = CHART()
chart2 = CHART(True)
chart1.plot_graph([[15.3,4.9], [21.3,6.7], [26.4,8.4], [29.4,9.4], [34,10.8]])
chart2.plot_graph([[15.3,4.9], [21.3,6.7], [26.4,8.4], [29.4,9.4], [34,10.8]])