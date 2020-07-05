import numpy 
import matplotlib.pyplot as plt
import random 
  
steps = 100000
x = numpy.zeros(steps) 
y = numpy.zeros(steps) 
  
for i in range(1, steps): 
    ran_n = random.randint(1, 4) 
    if ran_n == 1: 
        x[i] = x[i - 1] + 1
        y[i] = y[i - 1] 
    elif ran_n == 2: 
        x[i] = x[i - 1] - 1
        y[i] = y[i - 1] 
    elif ran_n == 3: 
        x[i] = x[i - 1] 
        y[i] = y[i - 1] + 1
    else: 
        x[i] = x[i - 1] 
        y[i] = y[i - 1] - 1
        
plt.figure(figsize=(6, 6))
plt.axis('equal')
plt.fill(x, y)
plt.show()
