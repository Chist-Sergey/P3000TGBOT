import session_functions


def write(username: str, chat_id: int) -> None:
    """
    Write data from a user session file to a database.

    It's a simple open-format-write-close operation.
    """
    # guard: prevent multiple database writings
    if search_by_name(username, chat_id):
        return None

    dates = session_functions.extract(username)

    # '[:-1]' == 'remove the last element' == 'remove a newline'
    day = dates[1][:-1]
    month = dates[2][:-1]

    data_row = f'{username} {day}.{month}\n'

    # 'a' == 'append' == 'write at the end of the file'
    database = open('databases/' + str(chat_id) + '.txt', 'a')
    database.write(data_row)
    database.close()


def remove(target_line: str, chat_id: int) -> None:
    """
    remove a line of user name
    and birthday date from a database text file.

    It's a simple open-remove-write-close operation.
    """
    # 'r' == 'read'
    database = open('databases/' + str(chat_id) + '.txt', 'r')
    # 'readlines' creates a list of strings
    # contains every line as a separate element
    # note that every string in list have
    # a newline (\n) at the end of it
    database_contents = database.readlines()
    database.close()

    # guard: target is not found
    if target_line not in database_contents:
        return None

    database_contents.remove(target_line)

    # stitch the list of strings back to a single string
    new_content = ''.join(database_contents)

    # 'w' == 'write' == 'remove old content, place new content'
    database = open('databases/' + str(chat_id) + '.txt', 'w')
    database.write(new_content)
    database.close()


def search_by_name(target: str, chat_id: int) -> str | None:
    """
    Search and retrive a matched string from a database text file.

    It's a simple O(n) search algorithm, checking one line at a time.

    Returns a whole line if the string is matched, None if not mached.
    """
    # 'r' == 'read'
    database = open('databases/' + str(chat_id) + '.txt', 'r')
    # 'readlines' creates a list of strings
    # contains every line as a separate element
    # note that every string in list have
    # a newline (\n) at the end of it
    database_contents = database.readlines()
    database.close()

    for line in database_contents:
        if target in line:
            return line

    return None


def search_by_date(target: str, chat_id: int) -> str | None:
    """
    Search and retrive all matched strings from a database text file.

    It's a simple O(n) search algorithm, checking one line at a time.

    Returns a string with all matches, None if not mached.
    """
    # 'r' == 'read'
    database = open('databases/' + str(chat_id) + '.txt', 'r')
    # 'readlines' creates a list of strings
    # contains every line as a separate element
    # note that every string in list have
    # a newline (\n) at the end of it
    database_contents = database.readlines()
    database.close()

    matches = ''
    for line in database_contents:
        if target in line:
            matches += line

    if not matches:
        return None

    return matches
