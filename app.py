ulist=[]
print('''user authentication application
	1.sign up
	2.log in
	3.delete user
	4.exit''')
while(True):
	choice=int(input("choice: "))
	if choice==1:
		user={}
		user['name']=input("name: ")
		user['pswd']=input("pswd: ")
		user['email']=input("email: ")
		ulist.append(user)
	if choice==2:
		uname=input("name: ")
		upswd=input("pswd: ")
		for u in ulist:
			if(u['name']==uname):
				if(u['pswd']==upswd):
					print("login successfull")
				else:
					print("loged in successfull")
			else:
				print("wrong username")
	if choice==3:
		username=input("enter user you want to delete:")
		for u in ulist:
			if u['name']==username:
				ulist.remove(u)
				print("user deleted")

	if choice==4:
		print("exit")

