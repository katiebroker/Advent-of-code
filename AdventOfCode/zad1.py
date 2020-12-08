


class Zadatak():

    def __init__(self):
        pass

    def compute(self):
        input_list = []
        with open('input1.txt', 'rt') as f:
            for line in f:
                input_list.append(line)

        input_list = [ char.rstrip('\n') for char in input_list ]
        print(input_list)
        for elem1 in input_list:
            for elem2 in input_list:
                print('elem1 = ' + elem1 + ' elem2 = ' + elem2)
                print(int(elem1) + int(elem2))
                if (int(elem1) + int(elem2) == 2020) :
                    return int(elem1) * int(elem2)
                    break