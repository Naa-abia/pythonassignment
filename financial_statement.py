funding = 50000
marketing_expense = funding * (25/100)
operational_expense = funding * (50/100)
current_balance = funding - (marketing_expense + operational_expense)

print("INCOME: {}".format(funding))
print("==EXPENSES==")
print("Marketing Expenses: {}".format(marketing_expense))
print("\tSocial media Marketing: {}\n".format(marketing_expense * (10 /100))) #\t is an escape sequence thast gives space . and \n gives space from the next line.
print("Operational Expenses: {}".format(operational_expense))

#print(current_balance)
#print(funding * (25/100))

print("\nwith a budget of {} Ahmed can acquire {} of customers\n".format(current_balance, int(current_balance/5))) #string interpolation which allows variables to put in strings at specific locations.