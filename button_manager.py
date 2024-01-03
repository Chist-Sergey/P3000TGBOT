class GeneralButtons:
    def button_continue():
        return ('Продолжить', 'continue',)


    def button_back():
        return ('Назад', 'back',)


    def button_abort():
        return ('Отмена', 'abort',)


    def button_finish():
        return ('Готово', 'finish',)


class Months:
    def button_11():
        return ('(1-3)\nЯнварь\nФевраль\nМарт', '13',)


    def button_12():
        return ('(4-6)\nАпрель\nМай\nИюнь', '46',)


    def button_21():
        return ('(7-9)\nИюль\nАвгуст\nСентябрь', '79',)


    def button_22():
        return ('(9-12)\nОктябрь\nНоябрь\nДекабрь', '90',)


class Months1:
    def button_11():
        return ('(1) Январь', '1',)


    def button_21():
        return ('(2) Февраль', '2',)


    def button_31():
        return ('(3) Март', '3',)


class Months2:
    def button_11():
        return ('(4) Апрель', '1',)


    def button_21():
        return ('(5) Май', '2',)


    def button_31():
        return ('(6) Июнь', '3',)


class Months3:
    def button_11():
        return ('(7) Июль', '1',)


    def button_21():
        return ('(8) Август', '2',)


    def button_31():
        return ('(9) Сентябрь', '3',)


class Months4:
    def button_11():
        return ('(10) Октябрь', '1',)


    def button_21():
        return ('(11) Ноябрь', '2',)


    def button_31():
        return ('(12) Декабрь', '3',)


# class Days:
#     def __init__(self, month):
#         max_days = (
#             0,
#             31, 28, 31,
#             30, 31, 30,
#             31, 31, 30,
#             31, 30, 31,
#         )
#         max_day = max_days[month]

#         return max_day
