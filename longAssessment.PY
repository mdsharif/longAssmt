import os
def cls():
	os.system('cls')
#TOTALMARKS FUNCTION
def totalMarks():
	sum = 0
	for each in score:
		sum = sum + score[each]
	return sum
#TOTAL MARKS END HERE

#HIGHSCORER
def highScore():
	highScore = 0
	for max in score:
		if(score[max]>highScore):
			highScore = score[max]
			highScorer = max
	return highScorer
#HIGH SCORE ENDS HERE		
#HIGHSCORER ENDS HERE
# RESULTS FUNCTION
def results():
	cls()
	print("**Results Of School**")
	print("  **Results Sheet**")
	print("RollNo.%15sName%16sScore" %("",""))	
	for roll in name:
		print("%-22d%-20s%-10d" %(roll,name[roll],score[roll]))
	print()	
# RESULTS END HERE

# SCOREOF FUNCTION
def scoreOf():
	cls()
	isFound = False
	print("**Score of A Student**")
	rollNumber = eval(input("Enter Ur Roll Number\t: "))
	cls()
	for roll in name:
		if(roll==rollNumber):
			print("Roll No.       : ",rollNumber)
			print("Student Name   : ",name[roll])
			print("Score	       : ",score[roll])
			isFound = True
	if(isFound==False):
		print("Incorrect Roll No.Try Again.\n")
# SCOREOF END HERE

# ADDNEW FUNCTION
def addNew():
	cls()
	print("**Adding the Detail's of a New Student**")
	rollNumber = eval(input("Ener Roll No.  : "))
	st_name = input("Enter Name     : ")
	st_score = eval(input("Enter Score    : "))
	name[rollNumber] = st_name
	score[rollNumber] = st_score
	print(st_name,"'s Detail Has been successfully Added to the Results List.\n")
	
#ADDNEW END HERE	

# SUMMARY FUNCTION
def summary():
	cls()
	print("**Summary of Result**")
	print("Total No. of Students   : ",len(name))
	highScorerRoll = highScore()
	print("Highest Score 		: ",score[highScorerRoll])
	print("Highest Scorer		: ",name[highScorerRoll])
	print("Average Score		: ",(totalMarks()/len(score)))
#	print("Pass Percentage		: ",passPer())

# MODIFY FUNCTION
def modify():
	cls()
	isFound = False
	rollModify = eval(input("Enter Roll Number Whose Result has to Update\t: "))
	for upd in score:
		if(rollModify == upd):
			isFound = True
			newScore = eval(input("Enter New Score\t: "))
			score[rollModify] = newScore
			print(name[rollModify],"'s Result Has Successfully Updated.\n")
	if(isFound == False):
		print("Incorrect Roll Number.Try Again.\n")
	print("under process modify")
# DELETE FUNCTION
def delete():
	cls()
#	isFound = False
#	rollN = eval(input("Enter Roll Number whose Record has to Be deleted\t: "))
#	for r in name:
#		if(r==rollN):
#			print(name)
#			isFound = True
#			del(name[r])
#			del(score[r])
#	if(isFound == False):
#		print("Roll Number is not Found.\n")
	print("under proces delete\n")
	print("More time Required to Complete this part of Code\n")
# TRANSFER
def transfer():
	fd = open('score.txt','w+')
	for each in name:
		fd.write(str(each)+":"+name[each]+":"+str(score[each])+"\n")
		
	print("The Result of All Students has been Successfully\nWritten to the Text File Named Score.txt\n")



##GLOBAL SCOPE
name  = {100101:'Priyanka',100102:'Lekha'}
score = {100101:60,100102:40} 


attempt = 0
confirm = True


cls()
while(confirm):
#	if(attempt==0):
#	print("*Talent International School Welcomes You.*\n")
#	else:
#	print()
	print("1.Results of All Students")
	print("2.Score of a Studens")
	print("3.Add Record of new Students")
	print("4.Summary of Result")
	print("5.Modify Score")
	print("6.Delete record of a Student")
	print("7.Transfer the Data to file")
	print("8.Close the Program")
	option = eval(input("\nEnter the Desired Option: "))
	if(option == 1):
		cls()
		results()
	elif(option == 2):
		cls()
		scoreOf()
	elif(option == 3):
		cls()
		addNew()
	elif(option == 4):
		cls()
		summary()
	elif(option == 5):
		cls()
		modify()
	elif(option == 6):
		cls()
		delete()
	elif(option == 7):
		cls()
		transfer()
	elif(option == 8):
		cls()
		print("Thanks for Using our Application.SEE U SOON.\n")
		confirm = False
	else:
		cls()
		attempt = attempt + 1
		if(attempt!=3):
			print("Print Wrong Number Has Entered.")
			print("U have only",(3-attempt)," attempt Left. OtherWise program will be closed Automatically.")
		else:
			print("You Have Reached Maximum Limit allowed.Program is Closing Now...")
			print("Program is Successfully Closed.")
			print("Thanks For Using Our Application.\n")
			confirm = False








