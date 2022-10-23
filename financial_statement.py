funding = 50000
marketing_expense = funding * (25/100)
operational_expense = funding * (50/100)
current_balance = funding - (marketing_expense + operational_expense)


#print(current_balance)
#print(funding * (25/100))

print("\nAHMED'S FINANCIAL STATEMENT")
print("\nFUNDING AMOUNT: {}".format(funding))
print("\n==EXPENSES==")
print("\nMarketing Expenses: {}".format(marketing_expense))
print("\t*Social media Marketing: {}".format(marketing_expense * (60 /100))) #\t is an escape sequence thast gives space . and \n gives space from the next line.
print("\t*Print Marketing: {}\n".format(marketing_expense * (40 /100)))
print("Operational Expenses: {}".format(operational_expense))
print("\t*Logistics: {}".format(operational_expense * (60 /100))) #\t is an escape sequence thast gives space . and \n gives space from the next line.
print("\t*Human Resource: {}".format(operational_expense * (40 /100))) #\t is an escape sequence thast gives space . and \n gives space from the next line.




print("\nWith a budget of {} Ahmed can acquire {} of customers\n".format(current_balance, int(current_balance/5))) #string interpolation which allows variables to put in strings at specific locations.