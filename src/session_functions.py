def start(username: str) -> None:
    """
    Use this once to initialize a session with the user.

    Creates a text file with a name of a user and
    fills it with starting data.
    """
    # '0\n0\n0\n' ==
    # 0         // step
    # 0         // month
    # 0         // day
    #           // empty space
    starting_data = '0\n0\n0\n'

    # 'w' == 'write' == 'remove old content, place new content'
    user_file = open(f'sessions/{username}.txt', 'w')
    user_file.write(starting_data)
    user_file.close()


def extract(username: str) -> list[str]:
    """
    Extract the user data from a text file.

    Converts a file data to a list of strings.

    Returns a list of strings
    """
    # 'r' == 'read'
    user_file = open(f'sessions/{username}.txt', 'r')
    user_data = user_file.readlines()
    user_file.close()

    return user_data


def write(username: str, session_data: list) -> None:
    """
    Write the session data in a text file.

    Converts a list of strings into a single string.
    """
    # stich up a list of strings to make a single string
    session_data = ''.join(session_data)

    # 'w' == 'write' == 'remove old content, place new content'
    user_file = open(f'sessions/{username}.txt', 'w')
    user_file.write(session_data)
    user_file.close()
