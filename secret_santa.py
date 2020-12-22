from random import shuffle

def randomized_dict(names_1,names_2):
    shuffle(names_1)
    shuffle(names_2)
    a_dict = dict(zip(names_1,names_2))
    for key in a_dict:
        if key == a_dict[key] or a_dict[a_dict[key]] == key: # person cannot be thir own secret santa. Nor can the receiver be the Secret Santa's Secret Santa
            return randomized_dict(names_1,names_2)
    return a_dict


def main():

    names_1 = []
    names_2 = []
    name = " "
    while name != "":
        name = input("Enter a Name  or Leave Blank and Press Enter If There Are No More Names to Enter: ")
        names_1.append(name)
    names_1.pop(-1)
    for element in names_1:
        names_2.append(element)

    a_dict = randomized_dict(names_1,names_2)


    print(a_dict)


main()
