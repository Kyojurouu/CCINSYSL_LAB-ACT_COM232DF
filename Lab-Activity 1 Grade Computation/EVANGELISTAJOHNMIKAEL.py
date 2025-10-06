import sys

# ACT 1
act1items = 30
while True:
   try:
       act1score = int(input("What's your score for Act 1? (0-30): "))
       if act1score > act1items or act1score < 0:
           print("Error: score can't be higher than items or lower than 0")
       else:
           break
   except ValueError:
       print("Error: please enter a number only.")

# ACT 2
act2items = 20
while True:
   try:
       act2score = int(input("What's your score for Act 2? (0-20): "))
       if act2score > act2items or act2score < 0:
           print("Error: score can't be higher than items or lower than 0")
       else:
           break
   except ValueError:
       print("Error: please enter a number only.")

# ACT 3
act3items = 10
while True:
   try:
       act3score = int(input("What's your score for Act 3? (0-10): "))
       if act3score > act3items or act3score < 0:
           print("Error: score can't be higher than items or lower than 0")
       else:
           break
   except ValueError:
       print("Error: please enter a number only.")

# Totals for acts
actTotalScore = act1score + act2score + act3score
actTotalItems = act1items + act2items + act3items

# ASSIGNMENT 1
as1items = 50
while True:
   try:
       as1score = int(input("What's your score for Assignment 1? (0-50): "))
       if as1score > as1items or as1score < 0:
           print("Error: score can't be higher than items or lower than 0")
       else:
           break
   except ValueError:
       print("Error: please enter a number only.")

# ASSIGNMENT 2
as2items = 50
while True:
   try:
       as2score = int(input("What's your score for Assignment 2? (0-50): "))
       if as2score > as2items or as2score < 0:
           print("Error: score can't be higher than items or lower than 0")
       else:
           break
   except ValueError:
       print("Error: please enter a number only.")

# ASSIGNMENT 3
as3items = 50
while True:
   try:
       as3score = int(input("What's your score for Assignment 3? (0-50): "))
       if as3score > as3items or as3score < 0:
           print("Error: score can't be higher than items or lower than 0")
       else:
           break
   except ValueError:
       print("Error: please enter a number only.")

# Totals for assignments
asTotalScore = as1score + as2score + as3score
asTotalItems = as1items + as2items + as3items

# Grand total for CS
allTotalScore = actTotalScore + asTotalScore
allTotalItems = actTotalItems + asTotalItems
csgrade = allTotalScore / allTotalItems * 100
csgrade2 = csgrade * 0.4

# LONG EXAM
longexamItems = 50
while True:
   try:
       longexamScore = int(input("What's your score for Long Exam? (0-50): "))
       if longexamScore > longexamItems or longexamScore < 0:
           print("Error: score can't be higher than items or lower than 0")
       else:
           break
   except ValueError:
       print("Error: please enter a number only.")
longexamGrade = longexamScore / longexamItems * 100
longexamGrade2 = longexamGrade * 0.4

# FINAL PROJECT
finalprojItems = 50
while True:
   try:
       finalprojScore = int(input("What's your score for Final Project? (0-50): "))
       if finalprojScore > finalprojItems or finalprojScore < 0:
           print("Error: score can't be higher than items or lower than 0")
       else:
           break
   except ValueError:
       print("Error: please enter a number only.")
finalprojGrade = finalprojScore / finalprojItems * 100
finalprojGrade2 = finalprojGrade * 0.2

# Final grade
finalGrade = csgrade2 + longexamGrade2 + finalprojGrade2

# TABLE OUTPUT
print("\nFINAL REPORT")
print(f"{' ':<15}{'SCORE':>6}{'ITEMS':>8}{'PERCENT':>10}{'WEIGHTED%':>12}")
print("-" * 52)
print(f"{'ACT1':<15}{act1score:>6}{act1items:>8}{(act1score/act1items*100):>10.2f}{'':>12}")
print(f"{'ACT2':<15}{act2score:>6}{act2items:>8}{(act2score/act2items*100):>10.2f}{'':>12}")
print(f"{'ACT3':<15}{act3score:>6}{act3items:>8}{(act3score/act3items*100):>10.2f}{'':>12}")
print(f"{'AS1':<15}{as1score:>6}{as1items:>8}{(as1score/as1items*100):>10.2f}{'':>12}")
print(f"{'AS2':<15}{as2score:>6}{as2items:>8}{(as2score/as2items*100):>10.2f}{'':>12}")
print(f"{'AS3':<15}{as3score:>6}{as3items:>8}{(as3score/as3items*100):>10.2f}{'':>12}")
print("-" * 52)
print(f"{'TOTAL (CS)':<15}{allTotalScore:>6}{allTotalItems:>8}{csgrade:>10.2f}{csgrade2:>12.2f}")
print(f"{'Long Exam':<15}{longexamScore:>6}{longexamItems:>8}{longexamGrade:>10.2f}{longexamGrade2:>12.2f}")
print(f"{'Final Project':<15}{finalprojScore:>6}{finalprojItems:>8}{finalprojGrade:>10.2f}{finalprojGrade2:>12.2f}")
print("-" * 52)
print(f"{'FINAL GRADE %':<31}{finalGrade:>10.2f}")
print("-" * 52)

# Pass/Fail message
if finalGrade < 60:
   print("You Unfortunately Failed")
else:
   print("You Passed!! Congratulations!")