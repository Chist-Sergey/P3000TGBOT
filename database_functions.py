def database_write(name: str, date) -> None:
    """
    Use this function to write a pair of user name
    and birthday date to a database text file.

    It's a simple open-write-close operation.

    This function returns nothing.
    This function doesn't raise any errors.
    """
    # 'a' == 'append' == 'apply at the end'
    with open('database.txt', 'a') as database:
        # 'f' == 'format' == 'replace names with their values'
        # '\n' == 'new line'
        data_row = f'{name} {date}\n'
        database.write(data_row)


def database_remove(target_line: str) -> None:
    """
    Use this function to remove a line of user name
    and birthday date from a database text file.

    It's a simple open-remove-close operation.

    This function returns nothing.
    This function doesn't raise any errors.
    """
    # 'r+' == 'reading and writing'
    with open('database.txt', 'r+') as database:
        # 'readlines' creates a list of strings,
        # contains every line as a separate element
        database_content = database.readlines()

        # a guard code in case the target is not found
        # if the guard code is passed, this means that
        # the target is in a database
        if target_line not in database_content:
            return None

        # remove a target string from a list of strings
        new_content = database_content.remove(target_line)
        # stich a list of strings back to a single string
        new_content = ''.join(new_content)

        # 'seek' == 'move a coursor' == 'set a writing point'
        # '0' == 'at the beginnig of the file'
        database.seek(0)
        database.write(new_content)


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
        database = database.readlines()

        matches = ''
        for line in database:
            if target in line:
                matches += line

        if matches == '':
            matches = None

        return matches
