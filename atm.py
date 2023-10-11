print('Введите сумму в рублях (от 1 до 100000): ')
money = int(input())
money2 = str(money)
money2 = list(money2)
length_money = len(money2)


def dozens():
    match money2[0]:
        case '9':
            print('Девяносто ')
        case '8':
            print('Восемьдесят ')
        case '7':
            print('Семьдесят ')
        case '6':
            print('Шестьдесят ')
        case '5':
            print('Пятьдесят ')
        case '4':
            print('Сорок ')
        case '3':
            print('Тридцать ')
        case '2':
            print('Двадцать ')
        case _:
            match money2[1]:
                case '9':
                    if length_money == 5:
                        print('Девятнадцать тысяч')
                    else:
                        print('Девятнадцать рублей')
                case '8':
                    if length_money == 5:
                        print('Восемнадцать тысяч')
                    else:
                        print('Восемнадцать рублей')
                case '7':
                    if length_money == 5:
                        print('Семнадцать тысяч')
                    else:
                        print('Семнадцать рублей')
                case '6':
                    if length_money == 5:
                        print('Шестнадцать тысяч')
                    else:
                        print('Шестнадцать рублей')
                case '5':
                    if length_money == 5:
                        print('Пятнадцать тысяч')
                    else:
                        print('Пятнадцать рублей')
                case '4':
                    if length_money == 5:
                        print('Четырнадцать тысяч')
                    else:
                        print('Четырнадцать рублей')
                case '3':
                    if length_money == 5:
                        print('Тринадцать тысяч')
                    else:
                        print('Тринадцать рублей')
                case '2':
                    if length_money == 5:
                        print('Двенадцать тысяч')
                    else:
                        print('Двенадцать рублей')
                case '1':
                    if length_money == 5:
                        print('Одиннадцать тысяч')
                    else:
                        print('Одиннадцать рублей')
                case _:
                    if length_money == 5:
                        print('Десять тысяч')
                    else:
                        print('Десять рублей')


def dozens2():
    match money2[-2]:
        case '9':
            print('девяносто ')
        case '8':
            print('восемьдесят ')
        case '7':
            print('семьдесят ')
        case '6':
            print('шестьдесят ')
        case '5':
            print('пятьдесят ')
        case '4':
            print('сорок ')
        case '3':
            print('тридцать ')
        case '2':
            print('двадцать ')
        case _:
            match money2[1]:
                case '9':
                    print('девятнадцать рублей')
                case '8':
                    print('восемнадцать рублей')
                case '7':
                    print('семнадцать рублей')
                case '6':
                    print('шестнадцать рублей')
                case '5':
                    print('пятнадцать рублей')
                case '4':
                    print('четырнадцать рублей')
                case '3':
                    print('тринадцать рублей')
                case '2':
                    print('двенадцать рублей')
                case '1':
                    print('одиннадцать рублей')
                case _:
                    print('десять рублей')


def units():
    match money2[0]:
        case '9':
            if length_money == 4:
                print('Девять тысяч ')
            else:
                print('Девять рублей')
        case '8':
            if length_money == 4:
                print('Восемь тысяч ')
            else:
                print('Восемь рублей')
        case '7':
            if length_money == 4:
                print('Семь тысяч ')
            else:
                print('Семь рублей')
        case '6':
            if length_money == 4:
                print('Шесть тысяч ')
            else:
                print('Шесть рублей')
        case '5':
            if length_money == 4:
                print('Пять тысяч ')
            else:
                print('Пять рублей')
        case '4':
            if length_money == 4:
                print('Четыре тысячи ')
            else:
                print('Четыре рубля')
        case '3':
            if length_money == 4:
                print('Три тысячи ')
            else:
                print('Три рубля')
        case '2':
            if length_money == 4:
                print('Две тысячи ')
            else:
                print('Два рубля')
        case _:
            if length_money == 4:
                print('Одна тысяча ')
            else:
                print('Один рубль')


def units3():
    match money2[-1]:
        case '9':
            if money2[-2] != '1':
                print('девять рублей')
        case '8':
            if money2[-2] != '1':
                print('восемь рублей')
        case '7':
            if money2[-2] != '1':
                print('семь рублей')
        case '6':
            if money2[-2] != '1':
                print('шесть рублей')
        case '5':
            if money2[-2] != '1':
                print('пять рублей')
        case '4':
            if money2[-2] != '1':
                print('четыре рубля')
        case '3':
            if money2[-2] != '1':
                print('три рубля')
        case '2':
            if money2[-2] != '1':
                print('два рубля')
        case _:
            if money2[-2] != '1':
                print('один рубль')


def hundreds():
    match money2[0]:
        case '9':
            print('Девятьсот ')
        case '8':
            print('Восемьсот ')
        case '7':
            print('Семьсот ')
        case '6':
            print('Шестьсот ')
        case '5':
            print('Пятьсот ')
        case '4':
            print('Четыреста ')
        case '3':
            print('Триста ')
        case '2':
            print('Двести ')
        case _:
            print('Сто ')


def hundreds2():
    match money2[-3]:
        case '9':
            print('девятьсот ')
        case '8':
            print('восемьсот ')
        case '7':
            print('семьсот ')
        case '6':
            print('шестьсот ')
        case '5':
            print('пятьсот ')
        case '4':
            print('четыреста ')
        case '3':
            print('триста ')
        case '2':
            print('двести ')
        case _:
            print('сто ')


def units2():
    match money2[1]:
        case '9':
            if money2[0] != '1':
                print('девять тысяч ')
        case '8':
            if money2[0] != '1':
                print('восемь тысяч ')
        case '7':
            if money2[0] != '1':
                print('семь тысяч ')
        case '6':
            if money2[0] != '1':
                print('шесть тысяч ')
        case '5':
            if money2[0] != '1':
                print('пять тысяч ')
        case '4':
            if money2[0] != '1':
                print('четыре тысячи ')
        case '3':
            if money2[0] != '1':
                print('три тысячи ')
        case '2':
            if money2[0] != '1':
                print('две тысячи')
        case '1':
            if money2[0] != '1':
                print('одна тысяча')
        case _:
            print(' ')


match length_money:
    case 6:
        if money == 100000:
            print('Сто тысяч рублей')
        else:
            print('Вы ввели некорректное число!')
    case 5:
        if money >= 1:
            dozens(), units2(), hundreds2(), dozens2(), units3()
        else:
            print('Вы ввели некорректное число!')
    case 4:
        if money >= 1:
            units(), hundreds2(), dozens2(), units3()
        else:
            print('Вы ввели некорректное число!')
    case 3:
        if money >= 1:
            hundreds(), dozens2(), units3()
        else:
            print('Вы ввели некорректное число!')
    case 2:
        if money >= 1:
            dozens(), units3()
        else:
            print('Вы ввели некорректное число!')
    case 1:
        if money >= 1:
            units()
        else:
            print('Вы ввели некорректное число!')
    case _:
        print('Вы ввели некорректное число!')
