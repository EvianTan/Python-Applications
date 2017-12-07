import random

for i in range(200):
	s = "abcdefghijklmnopqrstuvwxyz0123456789"
	passlen = 8
	p =  "".join(random.sample(s,passlen ))
	print str(i+1)+":"+p
