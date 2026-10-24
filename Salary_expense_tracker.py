user_monthly=int(input('Enter your monthly salary: '))
user_expenses=int(input('Enter your monthly expenses: '))
remaining_amount=user_monthly-user_expenses
print('Remaining Amount:',remaining_amount)
if user_monthly>0:
  savings_percentage=(remaining_amount/user_monthly)*100
  print('Savings percentage: ',savings_percentage)
else: 
  print('Savings percentage:',' cannot calculate')
if remaining_amount>=10000:
  print('Good Savings')
elif remaining_amount>=0:
  print('Low Savings')
else:
  print('Over Spending')
