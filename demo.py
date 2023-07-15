rans=0
wans=0
qlist =[]
print("quiz application: ")
print('''select your choice:
1.attempt quiz
2.add question
3.exit''')
ch=0
while(ch != 3):
	ch=int(input("enter your choice"))
	if ch == 1:
		print("attempt quiz")
		for q in qlist:
			print(q['qt'])
			print(q['a'])
			print(q['b'])
			print(q['c'])
			print(q['d'])
			ans= input("answer")
			if q['Cans']==ans:
				rans=rans+1
			else:
				wans=wans+1
				print("right ans: ",rans)
				print("wrong ans: ",wans)

	if ch==2:
					q={}
					q['qt']=input("enter question")
					q['a']=input("option a")
					q['b']=input("option b")
					q['c']=input("option c")
					q['d']=input("option d")
					q['Cans']=input("correct option")
					qlist.append(q)

