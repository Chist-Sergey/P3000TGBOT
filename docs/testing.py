"""
## Testing (manual)

How to use this testing template:

Copy an entire function you want to test from the code,
and paste it in a separate *.py file, then copy
and paste this template at the bottom of that file,
and edit it's contents to fit your needs.
"""

if __name__ == '__main__':
    # change here
    test_function = database_remove
    test_data_auto_amount = 10
    test_data_manual = [
        'asdfg 56.78',
        'sdlfk 76.58',
        'mkgtj 98.76',
        'sdfkl 37.84',
        'tbytj 93.85',
        'lkjli 27.38',
        'ChistovBackend 30.09',
    ]

    # generates a data row
    test_data_list = []
    for number in range(test_data_auto_amount):
        test_data = 'user{} {}.{}'.format(
            number,
            10 + number,
            12 + number,
        )
        test_data_list.append(test_data)

    # check the output in terminal
    print(f'\n\n{test_function}')
    print('\n\tGenerated Data\n')
    for test_data in test_data_list:
        print(
            f'{test_data} -> '
            f'{test_function(test_data)}'
        )
    print('\n\tManual Data\n')
    for test_data in test_data_manual:
        print(
            f'{test_data} -> '
            f'{test_function(test_data)}'
        )
