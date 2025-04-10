import os
import json
# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    subor= file_name
    with open(subor, "r") as file_obj:
        data=json.load(file_obj)
    sequential_data=data[field]
    return sequential_data
print(read_data("sequential.json","unordered_numbers"))

def linear_search(sequence,number):
    index = 0
    kanal= {}
    pozice= []
    for i in sequence:
        index +=1
        if i == number:
            pozice.append(index)
            kanal["index"] = pozice
            kanal["pocet"] = sequence.count(number)
    return kanal

def pattern_search(sequence,vzor):
    kanal={}
    pozice=[]
    delka=len(vzor)
    for i in range(len(sequence) - delka+1):
        if sequence[i:i + delka] in sequence:
            pozice.append(i)
    kanal["idx"]= pozice
    return kanal
def binary_search(sequence,cislo):
    for index,number in enumerate(sequence):
        if number == cislo:
            return print(f"čislo {cislo} se nachazi na pozici {index}")
        else:
            continue
    if cislo not in sequence:
        return print(f"None")



def main(file_name, field, number,vzor,):
     a = read_data(file_name, field)
     b = linear_search(a, number)
     c= pattern_search(a,vzor)
     d= binary_search(a,number)
     return print(f"{d}")



if __name__ == '__main__':
    main("sequential.json","unordered_numbers",8,"ATA")