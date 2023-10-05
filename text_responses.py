# Easy access to any bot text!
# I hope it will be replaced by far more
# superior message 'reactions'.

def greeting() -> str:
    return 'Опять работать.'


def write_success() -> str:
    return 'Запомнил.'


def write_fail() -> str:
    return 'Забыл дату.'


def write_exists() -> str:
    return 'Уже помню.'


def search_fail() -> str:
    return 'Не помню.'


def celebrate(people: str) -> str:
    return ('Помниться мне, сегодня надо кого-то поздравить!\n'
            f'{people}')
