# '\n' == 'new line' == 'make the text begin below the current text'

def sechude_active() -> str:
    return 'Опять работать.'


def sechude_active_already() -> str:
    return 'Уже работаю. Спасибо, что напомнили мне.'


def write_success() -> str:
    return 'Запомнил.\nПосмотреть ДР - /ya_rodilsa'


def write_exists() -> str:
    return 'Уже помню.\nПосмотреть ДР - /ya_rodilsa'


def search_fail() -> str:
    return 'Не помню.\nЗапомнить ДР - /ya_rodilsa'


def celebrate(people: str) -> str:
    return (
        'Помнится мне, сегодня надо кого-то поздравить!\n'
        # 'f' == 'format' == 'put variables in place of names'
        f'{people}'
    )


def remove_success() -> str:
    return 'Забыл.\nЗапомнить ДР - /ya_rodilsa'


def remove_fail() -> str:
    return 'Уже забыл.\nЗапомнить ДР - /ya_rodilsa'


def keyboard() -> str:
    return 'Когда у Вас ДР?'


def keyboard_final(username, session_data) -> str:
    # '[:-1]' == 'remove the last element' == 'remove a newline'
    day = session_data[1][:-1]
    month = session_data[2][:-1]
    # 'f' == 'format' == 'put variables in place of names'
    return f'Я запомню: "{username} {day}.{month}".'
