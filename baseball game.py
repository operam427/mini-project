def generate_numbers(n):
    import random

    numbers = []

    while len(numbers) < n:
        a = random.randint(0, 9)

        while a not in numbers:  # ' 서로 다른 번호 '
            numbers.append(a)

    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return (numbers)


def take_guess(n):
    numbers = []
    print("숫자 {}개를 하나씩 차례대로 입력하세요.".format(n))

    while len(numbers) < n:
        num = int(input("{}번째 숫자를 입력하세요: ".format(len(numbers) + 1)))

        while num < 0 or num > 9:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
            num = int(input("{}번째 숫자를 입력하세요: ".format(len(numbers) + 1)))

        while num in numbers:
            print("중복되는 숫자입니다. 다시 입력하세요.")
            num = int(input("{}번째 숫자를 입력하세요: ".format(len(numbers) + 1)))

        while num not in numbers:  # ' 서로 다른 번호 '
            numbers.append(num)

    return numbers


def get_score(guesses, solution):
    plus = []
    plus_2 = []

    for i in range(0, 3):
        if guesses[i] == solution[i]:
            plus.append(1)
        strike = len(plus)

    for i in range(0, 3):
        if guesses[i] in solution:
            plus_2.append(1)
        ball = len(plus_2) - len(plus)

    return ("{}S {}B".format(strike, ball))


gen = generate_numbers(3)
tak = take_guess(3)
print(get_score(gen, tak))

va = 1

if gen == tak:
    print("축하합니다. 1번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.")

else:
    while gen != tak:
        # gen = generate_numbers(3)
        tak = take_guess(3)
        print(get_score(gen, tak))
        va += 1
    print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(va))