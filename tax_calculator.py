def get_file_path():
    while True:
        # get file path from user
        path = str(input("Enter file path(taxtext.txt ) "))
        if path == "":
            # default file path
            file_path = "./taxtext.txt"
            break
        else:
            file_path = path
            break
    return file_path


def get_standard_deduction():
    if filling_status == '1':
        standard_deduction = 12200
    elif filling_status == '2':
        standard_deduction = 24400
    elif filling_status == '3':
        standard_deduction = 18350

    return standard_deduction


def get_taxes_due(income, standard_deduction):
    income_after_deduction = income - standard_deduction
    taxable_amounts = {'1': [9700, 39475, 84200, 160725, 204100, 510300],
                       '2': [19400, 78950, 168400, 321450, 408200, 612350],
                       '3': [13850, 52850, 84200, 160700, 204100, 510300]}
    taxes = [10, 12, 22, 24, 32, 35, 37]
    tax = 0
    i = 0
    if income_after_deduction >= 0:
        for taxable_amount in taxable_amounts[filling_status]:
            if income_after_deduction < taxable_amount:
                tax = taxes[i]
                break
            i += 1
        if tax == 0:
            tax = taxes[i]
    taxes_due = (income_after_deduction * tax) / 100
    return taxes_due


if __name__ == '__main__':
    while (True):
        try:
            # get file path from user
            file_path = get_file_path()
            # open file arcording to the path
            with open(file_path, 'r') as file:
                text_file_data = file.read().split('\n')
            break
        except:
            # re enter uer path if path is wrong
            print("You are enter file path is wrong enter currect file path")
            continue
    # income value get from file
    income = int(text_file_data[1])
    # get filling status from file
    filling_status = str(text_file_data[0])
    # going to get standard deduction...
    standard_deduction = get_standard_deduction()

    # going to get the taxes due...
    taxes_due = get_taxes_due(income, standard_deduction)

    print('\nYour standard deduction amount is $' + '{:,.2f}'.format(standard_deduction) +
          ' and your taxes due is $' + '{:,.2f}'.format(taxes_due))
