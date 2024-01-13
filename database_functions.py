from session_functions import session_user_data_extract

def database_write(username: str) -> None:
    """
    Use this function to write data from
    a user session file to a database.

    It's a simple open-format-write-close operation.

    This function returns nothing.
    This function doesn't raise any errors.
    """
    # guard condition to prevent multiple database writings
    if database_search_by_name(username):
        return None

    dates = session_user_data_extract(username)

    # '[:-1]' == 'remove the last element' == 'remove a newline'
    day = dates[1][:-1]
    month = dates[2][:-1]

    # 'a' == 'append' == 'write at the end of the file'
    database = open('database.txt', 'a')
    # 'f' == 'format' == 'put variables in place of names'
    # '\n' == 'new line' == 'make the text begin below the current text'
    data_row = f'{username} {day}.{month}\n'
    database.write(data_row)
    database.close()


def database_remove(target_line: str) -> None:
    """
    Use this function to remove a line of user name
    and birthday date from a database text file.

    It's a simple open-remove-write-close operation.

    This function returns nothing.
    This function doesn't raise any errors.
    """
    # 'r' == 'reading'
    database = open('database.txt', 'r')
    # 'readlines' creates a list of strings,
    # contains every line as a separate element
    # note that every string in list have
    # a newline (\n) at the end of it
    database_contents = database.readlines()
    database.close()

    # a guard code in case the target is not found
    # if the guard code is passed, this means that
    # the target is in a database
    if target_line not in database_contents:
        return None

    # remove a target string from a list of strings
    database_contents.remove(target_line)
    # stitch the list of strings back to a single string
    new_content = ''.join(database_contents)

    # 'w' == 'erase everything in file and start writing fresh'
    database = open('database.txt', 'w')
    database.write(new_content)
    database.close()


def database_search_by_name(target: str):
    """
    Use this function to search and retrive
    a matched string from a database text file.

    It's a simple O(n) search algorithm,
    checking one line at a time.

    This function returns a whole line if the
    string is matched, None if not mached.
    This function doesn't raise any errors.
    """
    with open('database.txt', 'r') as database:
        # 'readlines' creates a list of strings,
        # contains every line as a separate element
        # includes newlines (these -> '\n')
        database = database.readlines()

        for line in database:
            if target in line:
                return line

        return None


def database_search_by_date(target: str):
    """
    Use this function to search and retrive
    all matched strings from a database text file.

    It's a simple O(n) search algorithm,
    checking one line at a time.

    This function returns a string
    with all matches, None if not mached.
    This function doesn't raise any errors.
    """
    with open('database.txt', 'r') as database:
        # 'readlines' creates a list of strings,
        # contains every line as a separate element
        # includes newlines (these -> '\n')
        database = database.readlines()

        matches = ''
        for line in database:
            if target in line:
                matches += line

        if matches == '':
            matches = None

        return matches
