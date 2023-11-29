# Easy access to any bot text!
# I hope it will be replaced by far more
# superior message 'reactions'.

def sechude_active() -> str:
    return 'Опять работать.'


def write_success() -> str:
    return 'Запомнил.\nПосмотреть ДР - /kogda_dr'


def write_fail() -> str:
    return 'Не могу запомнить, когда не дописана дата.'


def write_exists() -> str:
    return 'Уже помню.\nПосмотреть ДР - /kogda_dr'


def search_fail() -> str:
    return 'Не помню.\nЗапомнить ДР - /ya_rodilsa'


def celebrate(people: str) -> str:
    return ('Помниться мне, сегодня надо кого-то поздравить!\n'
            f'{people}')


def remove_success() -> str:
    return 'Забыл.\nЗапомнить ДР - /ya_rodilsa'


def remove_fail() -> str:
    return 'Нельзя забыть того, чего не помнишь.'
