
def get_file_path():
    while True:
        path=str(input("Enter file path(taxtext.txt ) "))
        # C:\Users\ranga\PycharmProjects\text_input_to_file_read
        if path=="":
            file_path = "./taxtext.txt"
            break
        else:
            file_path=path
            break
        print(file_path)
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

    # getting input from the user...

    while(True):
        try:
            file_path = get_file_path()
            with open(file_path, 'r') as file:
                text_file_data = file.read().split('\n')
            break
        except:
            print("Enter currect file path")
            continue
    # income = get_income()
    income = int(text_file_data[1])
    # get filling status...
    # filling_status = get_filling_status()
    filling_status = str(text_file_data[0])
    # going to get standard deduction...
    standard_deduction = get_standard_deduction()

    # going to get the taxes due...
    taxes_due = get_taxes_due(income, standard_deduction)

    print('\nYour standard deduction amount is $' + '{:,.2f}'.format(standard_deduction) +
          ' and your taxes due is $' + '{:,.2f}'.format(taxes_due))
