numbers = []

while True:
    number = input('number ')
    if number != 'done':
        numbers.append(int(number))
        aver = sum(numbers)
        average = aver / len(numbers)
    elif number == 'done':
        print(average)
        break