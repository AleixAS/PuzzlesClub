#!/usr/bin/env python

data=open('data_projecteuler_problem8.txt')
data=data.readlines()
data=''.join(data)

number=input('\nHi buddy!\nHow many adjacent numbers are you looking for?: ')

products=[]
for i in range(0,len(data)):
	window=data[i:i+int(number)]
	products.append(window)

dict_products={}
list_products=[]
for val in products:
	product=1
	for i in val:
		product*=int(i)
	dict_products[product]=(val)
	list_products.append(product)

values_multiplied = tuple(dict_products[max(list_products)])

final_list=[]
for a in range(0,int(number)):
	final_list.append(values_multiplied[a])

print (' x '.join(final_list)+' = '+str(max(list_products)))
