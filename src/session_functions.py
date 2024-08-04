def session_start(username: str) -> None:
    """
    Use this once to initialize a session with the user.

    Creates a text file with a name of a user.
    Fills it with starting data.

    Returns nothing.
    Raises no errors.
    """
    # '0\n0\n0\n' ==
    # 0         // step
    # 0         // month
    # 0         // day
    #           // empty space
    # '\n' == 'new line' == 'make the text begin below the current text'
    starting_data = '0\n0\n0\n'

    with open(
        # 'f' == 'format' == 'put variables in place of names'
        file=f'user_data/{username}.txt',
        # 'w' == 'overwrite'
        mode='w',
    ) as user_file:

        user_file.write(starting_data)


def session_user_data_extract(username: str) -> list:
    """
    Extract the user data from a text file.

    Converts a file data to a list of strings.

    Returns a list of strings
    Raises no errors.
    """
    with open(
        # 'f' == 'format' == 'put variables in place of names'
        file=f'user_data/{username}.txt',
        # 'r' == 'read'
        mode='r',
    ) as user_file:

        user_data = user_file.readlines()

    return user_data


def session_user_data_write(username: str, session_data: list) -> None:
    """
    Write the session data in a text file.

    Converts a list of strings into a single string.

    Returns nothing.
    Raises no errors.
    """

    # stich up a list of strings to make a single string
    session_data = ''.join(session_data)

    with open(
        # 'f' == 'format' == 'put variables in place of names'
        file=f'user_data/{username}.txt',
        # 'w' == 'overwrite'
        mode='w',
    ) as user_file:

        user_file.write(session_data)
