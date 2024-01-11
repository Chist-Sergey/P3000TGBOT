from session_functions import session_user_data_extract

def database_write(username: str) -> None:
    """
    Use this function to write data from
    a user session file to a database

    It's a simple open-format-write-close operation.

    This function returns nothing.
    This function doesn't raise any errors.
    """
    dates = session_user_data_extract(username)

    day = dates[1]
    month = dates[2]

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

    # a newline is added to a 'target_line'
    # to match the contents of a 'database_contents',
    # as all elements in there have a newline,
    # but the target line does not
    # '\n' == 'newline' == 'text will begin in a new row below'
    # target_line += '\n'
    # NOTE: this line is disabled for the next reason:
    # 'database_search_by_name' returns a string with
    # a newline already attached to it
    # since there is no other function thar uses 'database_remove'
    # besides 'birthday_rm', this feature is no longer needed
    # horever, this may result in compatability problems in the future

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
