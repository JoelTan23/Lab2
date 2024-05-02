print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")


def display_main_menu():
    print("Enter some numbers separated by commas")

#Function was troubleshooted with chatgpt
def get_user_input():
    print("get_user_input")
    number_list_str = input()
    number_list = [float(x) for x in number_list_str.split(",")] # from chatgpt here --> need to study
    return number_list


def calc_average(number_list):
    print("calc_average")
    total = sum(number_list)
    average = total / len(number_list)
    print("average = " + str(average))
    return average


def find_min_max(number_list):
    print("find_min_max")
    maximum = max(number_list)
    minimum = min(number_list)
    maximum_minimum = (minimum, maximum)
    return maximum_minimum


def sort_temperature(number_list):
    print("sort_temperature")
    ascending = sorted(number_list)
    descending = sorted(number_list, reverse=True)
    return ascending, descending

#Function here was made with aid from chatgpt
def calc_median_temperature(number_list):
    print("calc_median_temperature")
    sorted_list = sorted(number_list)
    length = len(sorted_list)
    if length % 2 == 0:
        median = (sorted_list[length // 2] + sorted_list[length // 2 - 1]) / 2 #// divides with an int result, removing any remainder
    else:
        median = sorted_list[length // 2]
    return median


display_main_menu()

number_list = get_user_input()

average = calc_average(number_list)

maximum_minimum_tuple = find_min_max(number_list)
print("Minimum and maximum:", maximum_minimum_tuple)

ascendingList, descendingList = sort_temperature(number_list)
print("Ascending order:", ascendingList)
print("Descending order:", descendingList)

median = calc_median_temperature(number_list)
print("Median:", median)