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
    def jan_feb_mar():
        return ('(1-3)\nЯнварь\nФевраль\nМарт', '0',)


    def apr_may_jun():
        return ('(4-6)\nАпрель\nМай\nИюнь', '3',)


    def jul_aug_sep():
        return ('(7-9)\nИюль\nАвгуст\nСентябрь', '6',)


    def okt_nov_dec():
        return ('(10-12)\nОктябрь\nНоябрь\nДекабрь', '8',)


class Months1:
    def jan():
        return ('(1) Январь', '0',)


    def feb():
        return ('(2) Февраль', '1',)


    def mar():
        return ('(3) Март', '2',)


class Months2:
    def apr():
        return ('(4) Апрель', '0',)


    def may():
        return ('(5) Май', '1',)


    def jun():
        return ('(6) Июнь', '2',)


class Months3:
    def jul():
        return ('(7) Июль', '0',)


    def aug():
        return ('(8) Август', '1',)


    def sep():
        return ('(9) Сентябрь', '2',)


class Months4:
    def okt():
        return ('(10) Октябрь', '0',)


    def nov():
        return ('(11) Ноябрь', '1',)


    def dec():
        return ('(12) Декабрь', '2',)


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
