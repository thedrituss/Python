def doubleInteger(i):
    return i << 1


def find_smallest_int(arr):
    smallest = arr[0]
    for num in arr[1:]:
        if num < smallest:
            smallest = num
    return smallest

def find_smallest_int_min(arr):
    return min(arr)

def digitize(n):
    return [int(digit) for digit in str(n)[::-1]]

def bmi(weight, height):
    bmi_value = weight / (height ** 2)
    
    if bmi_value <= 18.5:
        return "Underweight"
    elif bmi_value <= 25.0:
        return "Normal"
    elif bmi_value <= 30.0:
        return "Overweight"
    else:
        return "Obese"

def fake_bin(x):
    return "".join("0" if int(digit) < 5 else "1" for digit in x)

def fake_bin(x):
    return "".join(["0" if int(digit) < 5 else "1" for digit in x])

def invert(lst):
    return [-x for x in lst]

def invert(lst):
    return list(map(lambda x: -x, lst))

def invert(lst):
    if not lst:
        return []
    return [-lst[0]] + invert(lst[1:])