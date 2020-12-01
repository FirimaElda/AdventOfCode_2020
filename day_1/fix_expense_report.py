import itertools


def find_both_numbers(expenselist):
    results = []
    for a, b in itertools.product(expenselist, expenselist):
        if (a + b) == 2020 and (a, b) not in results and (b, a) not in results:
            results.append((a, b))

    # print the results...
    for a, b in results:
        print(str(a) + ' + ' + str(b) + ' = 2020')
        print(str(a) + ' * ' + str(b) + ' = ' + str(a * b))


def find_three_numbers(expenselist):
    results = []
    for a, b, c in itertools.product(expenselist, expenselist, expenselist):
        if (a + b + c) == 2020 and (set((a, b, c)).issubset(set(results)) or not results):
            results.append((a, b, c))

    # print the results...
    for a, b, c in results:
        print(str(a) + ' + ' + str(b) + ' + ' + str(c) + ' = 2020')
        print(str(a) + ' * ' + str(b) + ' * ' + str(c) + ' = ' + str(a * b * c))


if __name__ == '__main__':
    f = open('sample_expense_report.txt', 'r')
    content = f.read()
    con_list = content.split('\n')
    con_list = [int(x) for x in con_list]
    print('Expense report: ' + str(con_list))
    find_both_numbers(con_list)
    find_three_numbers(con_list)

    f = open('my_expense_report.txt', 'r')
    content = f.read()
    con_list = content.split('\n')
    con_list = [int(x) for x in con_list]
    print('Expense report: ' + str(con_list))
    find_both_numbers(con_list)
    find_three_numbers(con_list)
