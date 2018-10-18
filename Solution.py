f=open('Input.txt','r')
for line in open('Input.txt'):
	l=f.readline()
	olist=l.split()
	rlist=[]
	for word in olist:
		if word[0]=='a' or word[0]=='e' or word[0]=='i' or word[0]=='o' or word[0]=='u' or word[0]=='y':
			rlist.append(word+'yay')
		else:
			for i in range(len(word)):
				if word[i]=='a' or word[i]=='e' or word[i]=='i' or word[i]=='o' or word[i]=='u' or word[i]=='y':
					rlist.append(word[i:]+word[:i]+'ay')
					break
	print(' '.join(rlist))