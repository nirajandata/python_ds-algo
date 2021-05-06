s="01:01:00AM"

def time_conv(s):
	t=int(s[0:2])
	if (s[-2:]=="AM"):
		t=12-t
	else:
		t=12+t
	return "{:02d}".format(t)+":"+s[3:-2]
		
	
		
print(time_conv(s))
