def numships(a, b):
	if (a == b):
		return 1;
	elif (a > b):
		return numships(b, a);
	elif (a == 0):
		return 0;
	else:
		return (b // a) + numships(b % a, a);

(a, b) = raw_input().split(' ')
print(numships(int(a), int(b)))