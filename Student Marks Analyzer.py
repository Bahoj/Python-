marks=[]
for i in range(5):
  user_marks=int(input('Enter your marks: '))
  if 0<=user_marks<=100:
   marks.append(user_marks)
  else:
    print('Invalid marks')
    break

print(marks)
print('Total marks: ',sum(marks))
avg_m=sum(marks)/len(marks)

print('Average marks',avg_m)
print('Highest Marks: ',max(marks))
print('Lowest Marks: ',min(marks))
if avg_m >=90 and avg_m <=100:
  print('Grade: A')
elif avg_m >=75 and avg_m <90:
  print('Grade: B')
elif avg_m >=60 and avg_m <75:
  print('Grade: C')
else:
  print('Grade: D')
if avg_m >=50:
  print('Result: Pass')
else:
  print('Result: Fail')

