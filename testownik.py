import os
import random
import time
import json

def loadSave():
	if "save.txt" in os.listdir():
		try:
			return json.loads(open("save.txt","r").readline())
		except:
			print("\n\033[1m\033[91mError in loading save file\033[0m")
	return False

def saveSave(toSave):
	try:
		with open("save.txt","w") as saveFile:
			saveFile.write(json.dumps(toSave))
	except:
		return False
	return True

def displayQue(txtName):
	answer=0
	boldFlag=False
	counter=0;
	with open(txtName,"r",1,"utf-8") as fileHandle:
		for line in fileHandle:
			if(line[0]=="X"):
				answer=line[1:len(line)-1]
				boldFlag=True
			else:
				if(boldFlag):
					print("\n\033[1m\033[93m",line,"\033[0m")
					boldFlag=False
				else:
					print(f"\t{counter}. {line}")
					counter+=1
	print(txtName)
	return answer

def ansStandarize(answer,noOfPossibilities):
	ansList=["0"]*noOfPossibilities
	for char in answer:
		try:
			ansList[int(char)]="1"
		except:
			print("Bad input.")
	return "".join(ansList)

def revAnsStandarize(answer):
	ansList=[]
	for i in range(0,len(answer)):
		if(answer[i]=="1"):
			ansList.append(str(i))
	return "".join(ansList)


# reading save file
pointList=[]
load=loadSave()
if(load):
	pointList=load[0]
	fileList=load[1]

else:
	# getting all answers files
	fileList=os.listdir()
	for fname in fileList:
		if ".txt" not in fname:
			fileList.remove(fname)
	pointList=[2]*len(fileList)

del load

while(sum(pointList)>0):
	drawn=random.randint(0,len(fileList)-1)
	if(pointList[drawn]>0):
		correctAnswer=displayQue(fileList[drawn])
		print(f"{pointList[drawn]}/2")
		try:
			userAnswer=input("Your answer: ")
			if correctAnswer==ansStandarize(userAnswer,len(correctAnswer)):
				pointList[drawn]-=1
				print("\033[92mCorrect answer.")
				time.sleep(1)
			else:
				pointList[drawn]+=1
				print("\033[91mBad answer. Correct was:",revAnsStandarize(correctAnswer),"\033[0m")
				time.sleep(1)
		except KeyboardInterrupt:
			print("\n\nSaving...")
			if(saveSave((pointList,fileList,))):
				print("\nSaved successfully. Exiting program.")
				exit(0)
			else:
				print("Cannot save. Do you have permission to save?")
				if(input("Exit anyway? y/N\n>> ") in ['y','Y']):
					exit(0)