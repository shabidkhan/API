import requests
import json ,os,pprint

while True:
	if os.path.exists("s_courses.json")==False:
		a=requests.get('http://saral.navgurukul.org/api/courses')
		pprint.pprint(a.text)
		b=a.text
		c=open('s_courses.json','w')
		json.dump(b,c)
		c.close()

	c=open('s_courses.json','r')
	jsl1=json.load(c)
	jsl2=json.loads(jsl1)
	print(type(jsl2))
	c.close()

	for i in jsl2:
		for j in range(len(jsl2[i])):
			if j<9:
				x='0'+str(j+1)
				print(x,'-',jsl2[i][j]['id'],' ','name -',jsl2[i][j]['name'])
			else:
				print(1+j,'-',jsl2[i][j]['id'],' ','name -',jsl2[i][j]['name'])

	j=int(input('enter no.'))
	print(j,'-',jsl2[i][j-1]['id'],' ','name -',jsl2[i][j-1]['name'],'\n')
	x=jsl2[i][j-1]['id']
	
	while True:
		
		a1=requests.get(' http://saral.navgurukul.org/api/courses/'+str(x)+'/exercises')
		b1=a1.text
		if os.path.exists("'exercises_'+str(x)+'.json'")==False:
			c1=open('exercises_'+str(x)+'.json','w+')
			json.dump(b1,c1)
			c1.close()
		c1=open('exercises_'+str	(x)+'.json','r')
		js1=json.load(c1)
		js2=json.loads(js1)
		c.close()
		for i in js2:
			for j in range(len(js2[i])):
				print('\t',j+1,'-',js2[i][j]['name'])
		inp=input('''
			*** YOU WANT TO 
			PRIVIOUS PAGE - THEN PRESS ("P")
			NEXT PAGE     - TNEN PRESS ("N")
			STARTING PAGE - THEN PRESS ("S")''').lower()
		if inp=='p':
			x-=1
		elif(inp=='n'):
			x+=1
		else:
			break
		if x<14:
			x=14
			print('have no PRIVIOUS PAGE ')
		elif(x>92):
			x=92
			print('have no NEXT PAGE')
		print('Id-',x)
	inp=input('**you want to exit then press "exit"').lower()
	if 'e' in inp:
		break	
