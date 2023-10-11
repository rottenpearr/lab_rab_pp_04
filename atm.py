print('Введите сумму в рублях: ')
money = int(input())
money2 = str(money)
money2 = list(money2)
length_money = len(money2)


def dozens():
    match money2[0]:
        case '9':
            print('Девяносто')
        case '8':
            print('Восемьдесят')
        case '7':
            print('Семьдесят')
        case '6':
            print('Шестьдесят')
        case '5':
            print('Пятьдесят')
        case '4':
            print('Сорок')
        case '3':
            print('Тридцать')
        case '2':
            print('Двадцать')
        case _:
            match money2[1]:
                case '9':
                    print('Девятнадцать')
                case '8':
                    print('Восемнадцать')
                case '7':
                    print('Семнадцать')
                case '6':
                    print('Шестнадцать')
                case '5':
                    print('Пятнадцать')
                case '4':
                    print('Четырнадцать')
                case '3':
                    print('Тринадцать')
                case '2':
                    print('Двенадцать')
                case '1':
                    print('Одиннадцать')
                case _:
                    print('Десять')


match length_money:
    case 6:
        print('Сто')
    case 5:
        dozens()
    case 4:
        match money2[0]:
            case '9':
                print('Девять тысяч')
            case '8':
                print('Восемь тысяч')
            case '7':
                print('Семь тысяч')
            case '6':
                print('Шесть тысяч')
            case '5':
                print('Пять тысяч')
            case '4':
                print('Четыре тысячи')
            case '3':
                print('Три тысячи')
            case '2':
                print('Две тысячи')
            case _:
                print('Одна тысяча')
    case 3:
        match money2[0]:
            case '9':
                print('Девятьсот')
            case '8':
                print('Восемьсот')
            case '7':
                print('Семьсот')
            case '6':
                print('Шестьсот')
            case '5':
                print('Пятьсот')
            case '4':
                print('Четыреста')
            case '3':
                print('Триста')
            case '2':
                print('Двести')
            case _:
                print('Сто')
    case 2:
        dozens()
