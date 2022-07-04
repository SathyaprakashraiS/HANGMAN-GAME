'''
def hscorechecker(score):
	for i in range(len(scores)):
		if(score>scores[i]):
			try:
				temp=scores[i]
				scores[i]=score
				#scores[i+1]=temp
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
				return 0
			except:
				temp=scores[i]
				scores[i]=score
				return 0
def display(scores):
	print(*scores)
score=1
scores=[7,6,4,2,0]
hscorechecker(score)
display(scores)
with open('highscore.txt', 'w') as f:
	for i in range(len(scores)):
		f.write(str(scores[i]))
		f.write('\n')
'''
tscores=[]
ttscores=[]
'''
with open('scorers.txt', encoding='utf8') as f:
	for line in f:
		if(line!='\n'):
			tscores.append(line)
		else:
			tscores.append("lo")
print(tscores)
'''
with open('highscore.txt', encoding='utf8') as f:
	for line in f:
		tscores.append(line[:-1])
		#if(line!='\n'):
		#	tscores.append(line[:-1])
print(tscores)