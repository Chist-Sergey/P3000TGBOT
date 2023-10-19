def database_remove(target: str) -> None:
    """
    Use this function to remove a line of user name
    and birthday date from a database text file.
    
    It get a list of all lines from a file,
    then, searches for a right line and then
    replaces it with None.

    This function returns nothing.
    This function doesn't raise any errors.
    """
    with open('database.txt', 'r') as database:
        extracted = database.readlines()
    print("before\n", extracted)
    extracted.remove(target)
    print("after\n", extracted)

    with open('database.txt', 'w') as database:
        for row in extracted:
            print("writing\n", row)
            database.write(row)
            database.write('\n')


if __name__ == '__main__':
    database_remove('567')
    database_remove('jkl')