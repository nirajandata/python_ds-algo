def log_search(base,value):
	log_val=0 
	while(value>1):
		value/=base
		#print(value)
		log_val=log_val+1
		if (value==1):
			return "the log is "+str(log_val)
	return 0
		
print(log_search(2,32))
