#!/usr/bin/env python


Pythagorean_list=[]

number=input('\nHi buddy!\nWhich product abc are you looking for?: ')


for a in range(1,int(number)+1):
	for b in range (2,int(number)+1):
		if b > a:
			for c in range (3,int(number)+1):
				if c > b:
					if ((a**2) + (b**2))==c**2:
						Pythagorean=[a,b,c]
						Pythagorean_list.append(Pythagorean)
				else:
					pass	
		else:
			pass

result=False
for pyt in Pythagorean_list:
	if pyt[0]+pyt[1]+pyt[2]==int(number):
		result = True
		print ('\nThe result is:   '+str({})+'^2 + '+str({})+'^2 = '+str({})+'^2 = '+str({})).format(pyt[0],pyt[1],pyt[2],pyt[2]**2)
		print ('\t\t'+str({})+' + '+str({})+' + '+str({})+' = '+str(number)+'\n').format(pyt[0],pyt[1],pyt[2])

if result == False:
	print ('\nDoesn\'t exists any one Pythagorean triplet for which a + b + c = '+str(number)+'\n')