# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
leap = "The year is leap"
not_leap = "The year is not leap"
if year % 4 == 0:
  if year % 100 != 0:
    print(leap)
else:
  print(not_leap)
if year % 100 == 0:
  if year % 400 == 0:
    print(leap)
  else:
    print(not_leap)  
