import numpy 
import matplotlib.pyplot as plt
import random 
  
steps = 100000
  
x = numpy.zeros(steps) 
y = numpy.zeros(steps) 
  
for i in range(1, steps): 
    val = random.randint(1, 4) 
    if val == 1: 
        x[i] = x[i - 1] + 1
        y[i] = y[i - 1] 
    elif val == 2: 
        x[i] = x[i - 1] - 1
        y[i] = y[i - 1] 
    elif val == 3: 
        x[i] = x[i - 1] 
        y[i] = y[i - 1] + 1
    else: 
        x[i] = x[i - 1] 
        y[i] = y[i - 1] - 1
        
plt.figure(figsize=(6, 6))
plt.axis('equal')
plt.fill(x, y)
plt.show()
