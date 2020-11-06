
def solution(roman):
    dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    number = 0
    index = 0
    while index < len(roman):
        if index == len(roman) - 1:
            number += dict[roman[index]]
            break
        elif dict[roman[index + 1]] > dict[roman[index]]:
            number += dict[roman[index + 1]] - dict[roman[index]]
            index += 2
        else:
            number += dict[roman[index]]
            index += 1
    return number


print(solution('MDCLXVI'))