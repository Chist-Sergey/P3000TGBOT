def session_start(username: str) -> None:
    """
    Use this once to initialize a session with the user.

    Returns nothing.
    Raises no errors.
    """
    # '1\n1\n1\n1900' ==
    # 1
    # 1
    # 1
    # 1900
    starting_data = '1\n1\n1\n1900'

    with open(
    # 'f' == 'format' == 'put variables in place of names'
        file=f'user_data/{username}.txt',
        # 'w' == 'write'
        mode='w',
    ) as user_file:
        user_file.write(starting_data)


def session_user_data_extract(username: str) -> list:
    """
    Extract the user data from a text file.

    Converts a file data to a list of strings,
    and then to a list of integers.

    Returns a list of integers
    Raises no errors.
    """
    user_data = open(
        # path to file and its extenstion
        # 'f' == 'format' == 'put variables in place of names'
        file=f'user_data/{username}.txt',
        # 'r' == 'read'
        mode='r',
    ).readlines()

    # convert a list of strings to a list of integers
    user_data = list(map(int, user_data))

    return user_data


def session_user_data_write(username: str, session_data: list) -> None:
    """
    Write the session data in a text file.

    Converts a list of integers into a list of strings,
    stiches it to get a whole string with newlines.

    Returns nothing.
    Raises no errors.
    """
    # convert a list of integers to a list of strings
    session_data = list(map(str, session_data))

    # stich up a list if strings to make a single string
    session_data = '\n'.join(session_data)

    open(
        # 'f' == 'format' == 'put variables in place of names'
        file=f'user_data/{username}.txt',
        # 'w' == 'write'
        mode='w',
    ).write(session_data)

    return session_data
