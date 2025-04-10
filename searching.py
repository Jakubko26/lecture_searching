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
def main(file_name,field,number):
    a= read_data(file_name,field)
    b= linear_search(a,number)
    return print(f"{b}")


if __name__ == '__main__':
    main("sequential.json","unordered_numbers",0)