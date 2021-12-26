# 최종

def generate_numbers(n):
    import random

    numbers = []

    while len(numbers) < n:
        a = random.randint(1, 45)

        while a not in numbers:  # ' 서로 다른 번호 '
            numbers.append(a)

    return (numbers)

def draw_winning_numbers(n):
    six = generate_numbers(n)
    new_list = sorted(six)

    import random
    bonus = random.randint(1, 45)

    if bonus not in new_list:  # ' 서로 다른 번호
        new_list.append(bonus)
    return new_list


# print(draw_winning_numbers(6))

def count_matching_numbers(list_1, list_2):
    num = 0

    for i in range(len(list_2)):
        if list_2[i] in list_1:
            num += 1
        # else :
        # num += 0   # else 굳이 안 써도 됨!
    return num

def check(list_1, list_2):
    num = count_matching_numbers(list_1, list_2)
    len_a = len(list_1)
    len_b = len(list_2)

    if list_1[0:len_a] == list_2[0:len_b - 1]:
        return (1000000000)

    elif (num == 6 and list_2[-1] in list_1):
        return (50000000)

    elif (num == 5 and list_2[-1] not in list_1):
        return (1000000)

    elif (num == 4 and list_2[-1] not in list_1) or (num == 5 and list_2[-1] in list_1):
        return (50000)

    elif (num == 3 and list_2[-1] not in list_1) or (num == 4 and list_2[-1] in list_1):
        return (5000)
    else:
        return 0


numbers_test = generate_numbers(6)
winning_numbers_test = draw_winning_numbers(6)
count_matching_numbers(numbers_test, winning_numbers_test)
check(numbers_test, winning_numbers_test)

#print(numbers_test, winning_numbers_test)
print(check(numbers_test, winning_numbers_test))

