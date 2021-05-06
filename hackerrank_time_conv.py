s="01:01:00AM"

def time_conv(s):
        t=int(s[0:2])%12+(s[-2:]=="PM")*12
	return "{:02d}".format(t)+":"+s[3:-2]
	
		
	
		
print(time_conv(s))
