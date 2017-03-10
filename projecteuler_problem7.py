#!/usr/bin/env python

import itertools

def prime_number_at_X():
	number=input('\nHi buddy!\nWhat \'X\'st prime number are you looking for?: ')
	counter = 0 # Set counter to 0
	for num in itertools.count(+1): # look from 0 to infinity
		if counter <number: # While counter (number of prime number) is lower than 'X' do something, otherwise stop.
			for i in range(2,num):			
				if (num % i) == 0: # if number isn't prime, break
					break
			else: # if number is prime +1
				counter += 1
		else:
			break
	return (num-1) # Return last number (-1) when it realize counter is not < X


print prime_number_at_X()

