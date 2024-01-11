def sechude_active() -> str:
    return 'Опять работать.'


def write_success() -> str:
    return 'Запомнил.\nПосмотреть ДР - /ya_rodilsa'


def write_exists() -> str:
    return 'Уже помню.\nПосмотреть ДР - /ya_rodilsa'


def search_fail() -> str:
    return 'Не помню.\nЗапомнить ДР - /ya_rodilsa'


def celebrate(people: str) -> str:
    return ('Помниться мне, сегодня надо кого-то поздравить!\n'
            f'{people}')


def remove_success() -> str:
    return 'Забыл.\nЗапомнить ДР - /ya_rodilsa'


def remove_fail() -> str:
    return 'Уже забыл.\nЗапомнить ДР - /ya_rodilsa'


def birthday_set_keyboard_text() -> str:
    return 'Введите дату своего ДР, используя кнопки на сообщении:'


def birthday_set_keyboard_final_text(username, session_data) -> str:
    return f'Я запомню: "{username} {session_data[1]}.{session_data[2]}".'
