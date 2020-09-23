def get_second_largest_element(array):
    """Return the second largest number from the array"""

    arr_size = len(array)
    if arr_size < 2:
        # print("Invalid Input: Array with atleast size 2 is required ")
        return -1

    largest = second_largest = -214748364802

    for value in range(arr_size):
        if array[value] > largest:
            second_largest = largest
            largest = array[value]
        elif array[value] > second_largest and array[value] != largest:
            second_largest = array[value]

    if second_largest == -214748364802:
        return -1
    else:
        return second_largest


if __name__ == "__main__":

    string_array = ["-214748364802", "-214748364802"]
    array = list(map(int, string_array))
    assert -1 == get_second_largest_element(array)
