import pandas as pd


def multiplication_table(num):
    # Return a multiplication table from a number
    table = []
    for i in range(11):
        table.append(f'{num} * {i} = {i * num}')
        i += 1
    return table


try:
    num = int(
        input('Enter a number to get the multiplication table for that number -> '))

    table_number = pd.DataFrame({
        # The function multiplication_table() is called and it reslt is used inside a data frame to make a table with the result
        f'Multiplication Table for {num}': multiplication_table(num)
    })
    print(table_number)
except:
    print('You must to a real number')
