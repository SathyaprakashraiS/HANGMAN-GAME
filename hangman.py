import os
import time
from words import *
import random
word="hangman"
difficulty="EASY"
instruction=""
scores=[]
names=[]
difficulty=""
score=-100
menu=True
diffoption=False
result=False
with open('instruction.txt', encoding='utf8') as f:
	for line in f:
		instruction+=line
		#print(line.strip())
'''
with open('highscore.txt', encoding='utf8') as f:
	for line in f:
		scores.append(line)
		#print(line.strip())
'''
with open('highscore.txt', encoding='utf8') as f:
	for line in f:
		if(line!='\n'):
			scores.append(line[:-1])
		else:
			scores.append(0)
with open('difficulty.txt', encoding='utf8') as f:
	for line in f:
		difficulty+=line
		#print(line.strip())
with open('scorers.txt', encoding='utf8') as f:
	for line in f:
		if(line!='\n'):
			line=line.replace("\n","")
			names.append(line)
		else:
			names.append("")
def scoreboard():
	for i in range(len(scores)):
		'''
		liner=""
			liner+=str(i+1)+"> "+str(names[i])+" : "+str(scores[i])
			print(liner)
		'''
		if(int(scores[i])==0 and str(names[i])==""):
			liner=""
			liner+=str(i+1)+"> "+"RECORD AINT MADE YET"
			print(liner)
			#print(str(i+1),"> ","RECORD AINT MADE YET")
		else:
			liner=""
			liner+=str(i+1)+"> "+str(names[i])+" : "+str(scores[i])
			print(liner)
def hscorechecker(score):
	global scores
	ss=False
	loc=0
	for i in range(len(scores)):
		if(int(score)>int(scores[i])):
			ss=True
			try:
				temp=scores[i]
				scores[i]=score
				loc=i
				display(scores)
				flag=True
				for j in range(i+1,len(scores)):
					if(flag):
						ntemp=scores[j]
						scores[j]=temp
						flag=False
						print(temp,scores[j],ntemp)
					else:	
						temp=scores[j]
						scores[j]=ntemp
						flag=True
						print("0",temp,scores[j],ntemp)
				return ss,scores,loc
			except:
				temp=scores[i]
				scores[i]=score
				loc=i
				return ss,scores,loc
	return ss,scores,loc
def continuer(score):
	global names
	print("SCORE:",score)
	v=input("continue game (y/n)")
	if(v=="y" or v=="Y" or v=="yes" or v=="YES"):
		return True
	else:
		ss,scores,loc=hscorechecker(score)
		if(ss):
			print("A highscore is detected and is been added to the list")
			b=input("Enter your name to write on the score board")
			names[loc]=b
			print("SCORE BOARD")
			print(*scores)
			with open('highscore.txt', 'w') as f:
				for i in range(len(scores)):
					f.write(str(scores[i]))
					f.write("\n")
				#f.write(scores)
			with open('scorers.txt', 'w') as f:
				for i in range(len(names)):
					f.write(str(names[i]))
					f.write("\n")
				#f.write(names)
			quit()
			#return False
		else:
			print("THANK YOU FOR PLAYING")
			quit()
			#return False
def found(difficulty,score):
	os.system("cls")
	ttrue=False
	print("YOU WON!")
	if(difficulty=="EASY"):
		score+=5
		ttrue=continuer(score)
		return ttrue,score
	elif(difficulty=="MEDIUM"):
		score+=15
		ttrue=continuer(score)
		return ttrue,score
	elif(difficulty=="HARD"):
		score+=25
		ttrue=continuer(score)
		return ttrue,score
	else:
		score+=40
		ttrue=continuer(score)
		return ttrue,score
	print("SCORE:",score)
	'''
	v=input("continue game (y/n)")
	if(v=="y" and v=="Y" and v=="yes" and v=="YES"):
		pass
	else:
		ss,scores,loc=hscorechecker(score)
		if(ss):
			print("A highscore is detected and is been added to the list")
			b=input("Enter your name to write on the score board")
			names[loc]=b
			print("SCORE BOARD")
			print(*scores)
			with open('highscore.txt', 'w') as f:
				f.write(scores)
			with open('scorers.txt', 'w') as f:
				f.write(names)
		else:
			print("THANK YOU FOR PLAYING")
	'''
def diffcheck(difficulty):
	if(difficulty=="EASY" or difficulty=="MEDIUM" or difficulty=="HARD" or difficulty=="EXTREME"):
		return difficulty
	else:
		difficulty="EASY"
		return difficulty
difficulty=diffcheck(difficulty)
word=word.upper()
tries=8
mistakes=0
q=[[None for y in range(1) ]for x in range(5)]
ans=["_"]*len(word)
tans=""
guessedletters=""
clue=0
anslen=len(word)
def weever(ans):
	tans=""
	for i in range(len(ans)):
		tans+=str(ans[i])
	return tans
def quit():
	print("QUITTING...")
	time.sleep(1)
	os._exit(0)
def dispclue(q,clue):
	for i in range(clue):
		print(i+1,"> ",q[i])
	print("")
def dispnedpic():
	endpic=[
["","-","-","-","-","-","-","-","","",],
["","|","","","","","|","","","",],
["","|","","","","","0","","","",],
["","|","","","-","|","-","","","",],
["","|","","","","","|","","","",],
["","|","","","","/","\\","","","",],
["","|","","","","","","","","",],
["","|","","","","","","","","",],
["-","-","-","","","","","","","",]
]
	for i in range(9):
		for j in range(9):
			print(endpic[i][j],end=" ")
		print(" ")
def checker(theinp,guessedletters,tries,mistakes,ans,clue,difficulty,score,result):
	try:
		theinp=theinp.upper()
	except:
		theinp=theinp
		print("IN EXCEPTION")
	if theinp in guessedletters:
		print("already guessed")
		return guessedletters,ans,tries,mistakes,clue,difficulty,score,result
	elif theinp in word:
		guessedletters+=theinp
		for i in range(len(word)):
			if(word[i]==theinp):
				ans[i]=theinp.upper()
			tans=weever(ans)
		if(tans==word):
			result,score=found(difficulty,score)
		return guessedletters,ans,tries,mistakes,clue,difficulty,score,result
	else:
		tries-=1
		mistakes+=1
		if(clue==0 and (tries%2!=0)):
			clue+=2
			print("wrong guess")
			return guessedletters,ans,tries,mistakes,clue,difficulty,score,result
		if(clue!=5 and (tries%2!=0)):
			clue+=1
		print("wrong guess")
		return guessedletters,ans,tries,mistakes,clue,difficulty,score,result
def display(tries):
	if(tries==7):
		endpic=[
	["","","","","","","","","","",],
	["","","","","","","","","","",],
	["","","","","","","","","","",],
	["","","","","","","","","","",],
	["","","","","","","","","","",],
	["","","","","","","","","","",],
	["","","","","","","","","","",],
	["","","","","","","","","","",],
	["-","-","-","","","","","","","",]
	]
		for i in range(9):
			for j in range(9):
				print(endpic[i][j],end=" ")
			print(" ")
	elif(tries==6):
		endpic=[
["","","","","","","","","","",],
["","|","","","","","","","","",],
["","|","","","","","","","","",],
["","|","","","","","","","","",],
["","|","","","","","","","","",],
["","|","","","","","","","","",],
["","|","","","","","","","","",],
["","|","","","","","","","","",],
["-","-","-","","","","","","","",]
]
		for i in range(9):
			for j in range(9):
				print(endpic[i][j],end=" ")
			print(" ")
	elif(tries==5):
		endpic=[
["","-","-","-","-","-","-","-","","",],
["","|","","","","","","","","",],
["","|","","","","","","","","",],
["","|","","","","","","","","",],
["","|","","","","","","","","",],
["","|","","","","","","","","",],
["","|","","","","","","","","",],
["","|","","","","","","","","",],
["-","-","-","","","","","","","",]
]
		for i in range(9):
			for j in range(9):
				print(endpic[i][j],end=" ")
			print(" ")
	elif(tries==4):
		endpic=[
["","-","-","-","-","-","-","-","","",],
["","|","","","","","|","","","",],
["","|","","","","","","","","",],
["","|","","","","","","","","",],
["","|","","","","","","","","",],
["","|","","","","","","","","",],
["","|","","","","","","","","",],
["","|","","","","","","","","",],
["-","-","-","","","","","","","",]
]
		for i in range(9):
			for j in range(9):
				print(endpic[i][j],end=" ")
			print(" ")
	elif(tries==3):
		endpic=[
["","-","-","-","-","-","-","-","","",],
["","|","","","","","|","","","",],
["","|","","","","","0","","","",],
["","|","","","","","","","","",],
["","|","","","","","","","","",],
["","|","","","","","","","","",],
["","|","","","","","","","","",],
["","|","","","","","","","","",],
["-","-","-","","","","","","","",]
]
		for i in range(9):
			for j in range(9):
				print(endpic[i][j],end=" ")
			print(" ")
	elif(tries==2):
		endpic=[
["","-","-","-","-","-","-","-","","",],
["","|","","","","","|","","","",],
["","|","","","","","0","","","",],
["","|","","","","","|","","","",],
["","|","","","","","|","","","",],
["","|","","","","","","","","",],
["","|","","","","","","","","",],
["","|","","","","","","","","",],
["-","-","-","","","","","","","",]
]
		for i in range(9):
			for j in range(9):
				print(endpic[i][j],end=" ")
			print(" ")
	elif(tries==1):
		endpic=[
["","-","-","-","-","-","-","-","","",],
["","|","","","","","|","","","",],
["","|","","","","","0","","","",],
["","|","","","","","|","","","",],
["","|","","","","","|","","","",],
["","|","","","","/","\\","","","",],
["","|","","","","","","","","",],
["","|","","","","","","","","",],
["-","-","-","","","","","","","",]
]
		for i in range(9):
			for j in range(9):
				print(endpic[i][j],end=" ")
			print(" ")
	else:
		print(" ")
def diffwriter(difficulty):
	with open('difficulty.txt', 'w') as f:
		f.write(difficulty)
def trycheck(difficulty):
	if(difficulty=="EASY"):
		tries=10
		diffwriter(difficulty)
		return tries
	elif(difficulty=="MEDIUM"):
		tries=8
		diffwriter(difficulty)
		return tries
	elif(difficulty=="HARD"):
		tries=6
		diffwriter(difficulty)
		return tries
	elif(difficulty=="EXTREME"):
		tries=4
		diffwriter(difficulty)
		return tries
	else:
		difficulty="EASY"
		tries=4
		diffwriter(difficulty)
		return tries
tries=trycheck(difficulty)
diffwriter(difficulty)
def guesscount():
	return len(ans)
def blanker(word,guessedletters):
	for i in (word):
		if(i in guessedletters):
			print(i.upper(),end=' ')
		else:
			print("_",end=' ')
	print("")
gussed=guesscount()
def selector():
	num=random.randint(0,9)
	word=""
	q=[[None for y in range(1) ]for x in range(5)]
	word=twords[num]
	word=word.upper()
	for i in range(5):
		q[i]=tclues[num][i]
	return word,q 
def setgame():
	global word,tries,mistakes,q,ans,tans,guessedletters,clue,anslen,difficulty,tries,result
	word="test"
	word=word.upper()
	selector()
	tries=8
	mistakes=0
	q=[[None for y in range(1) ]for x in range(tries)]
	word,q=selector()
	ans=["_"]*len(word)
	tans=""
	guessedletters=""
	clue=0
	anslen=len(word)
	difficulty=diffcheck(difficulty)
	tries=trycheck(difficulty)
	diffwriter(difficulty)
	result=False
while(menu):
	#hangman hanging picture
	os.system("cls")
	print("1>PLAY GAME")
	print("2>CHOOSE DIFFICULTY")
	print("3>SHOW INSTRUCTION")
	print("4>HIGH SCORE")
	print("5>EXIT")
	print("")
	z=input("enter the option: ")
	if(int(z)==1):
		menu=False
		setgame()
	elif(int(z)==2):
		diffoption=True
		while(diffoption):
			os.system("cls")
			print("CURRENT DIFFICULTY: ",difficulty)
			print("")
			resp=input("Change Difficulty (y/n): ")
			if(resp=="y" or resp=="Y" or resp=="yes"):
				print("1.EASY\n2.MEDIUM\n3.HARD\n4.EXTREME\n5.<-Back")
				x=input("choose difficulty: ")
				try:
					if(int(x)==1):
						diffoption=False
						difficulty="EASY"
					elif(int(x)==2):
						diffoption=False
						difficulty="MEDIUM"
					elif(int(x)==3):
						diffoption=False
						difficulty="HARD"
					elif(int(x)==4):
						diffoption=False
						difficulty="EXTREME"
					else:
						print("INVALID INPUT")
						time.sleep(1.5)
						diffoption=True
				except:
					print("INVALID INPUT")
					time.sleep(1.5)
					diffoption=True
			else:
				diffoption=False
				menu=True
	elif(int(z)==3):
		os.system("cls")
		print("INSTRUCTIONS")
		print(instruction)
		input()
	elif(int(z)==4):
		os.system("cls")
		print("HIGH SCORE")
		scoreboard()
		input("")
	elif(int(z)==5):
		quit()
		#os._exit(0)
	else:
		print("INVALID INPUT 0")
		time.sleep(1)
		menu=True
	'''
	try:
		if(int(z)==1):
			menu=False
			setgame()
		elif(int(z)==2):
			diffoption=True
			while(diffoption):
				os.system("cls")
				print("CURRENT DIFFICULTY: ",difficulty)
				print("")
				resp=input("Change Difficulty (y/n): ")
				if(resp=="y" or resp=="Y" or resp=="yes"):
					print("1.EASY\n2.MEDIUM\n3.HARD\n4.EXTREME\n5.<-Back")
					x=input("choose difficulty: ")
					try:
						if(int(x)==1):
							diffoption=False
							difficulty="EASY"
						elif(int(x)==2):
							diffoption=False
							difficulty="MEDIUM"
						elif(int(x)==3):
							diffoption=False
							difficulty="HARD"
						elif(int(x)==4):
							diffoption=False
							difficulty="EXTREME"
						else:
							print("INVALID INPUT")
							time.sleep(1.5)
							diffoption=True
					except:
						print("INVALID INPUT")
						time.sleep(1.5)
						diffoption=True
				else:
					diffoption=False
					menu=True
		elif(int(z)==3):
			os.system("cls")
			print("INSTRUCTIONS")
			print(instruction)
			input()
		elif(int(z)==4):
			os.system("cls")
			print("HIGH SCORE")
			scoreboard()
			input("")
		elif(int(z)==5):
			quit()
			#os._exit(0)
		else:
			print("INVALID INPUT 0")
			time.sleep(1)
			menu=True
	except:
		print("INVALID INPUT")
		time.sleep(1)
		menu=True
	'''
'''
def diffwriter(difficulty):
	with open('difficulty.txt', 'w') as f:
		f.write(difficulty)
def trycheck(difficulty):
	if(difficulty=="EASY"):
		tries=10
		diffwriter(difficulty)
		return tries
	elif(difficulty=="MEDIUM"):
		tries=8
		diffwriter(difficulty)
		return tries
	elif(difficulty=="HARD"):
		tries=6
		diffwriter(difficulty)
		return tries
	elif(difficulty=="EXTREME"):
		tries=4
		diffwriter(difficulty)
		return tries
	else:
		difficulty="EASY"
		tries=4
		diffwriter(difficulty)
		return tries
tries=trycheck(difficulty)
diffwriter(difficulty)
'''
while(tries!=0 and menu==False):
	os.system('cls')
	if(result):
		setgame()
	else:
		print("GUESS THE WORD!")
		blanker(word,guessedletters)
		print("number of guesses left: ",tries)
		print("HANG MAN")
		display(tries)
		if(clue==0):
			print("CLUE")
			print("1>",q[0])
		else:
			print("CLUE")
			dispclue(q,clue)
		theinp=input("enter the letter you guessed: ")
		guessedletters,ans,tries,mistakes,clue,difficulty,score,result=checker(theinp,guessedletters,tries,mistakes,ans,clue,difficulty,score,result)
		print("WORD:",*ans)
if(tries<=0 and menu==False):
	os.system('cls')
	print("GAME OVER")
	dispnedpic()
	print("CLUES")
	dispclue(q,5)
	print("YOUR GUESS: ",*ans)
	print("THE WORD: ",word)

