import numpy as np
import math 
import matplotlib.pyplot as plt
%matplotlib inline 

def inverseCDFExponential(N,k):
    probArray=np.random.uniform(0,1,N)
    x = []
    for p in probArray :
        prob = (math.log(1-p))/(-1 * k)
        x.append(prob)   
    return x

xValues = inverseCDFExponential(100,4) 
xValuesnp = np.array(xValues)
plt.hist(xValuesnp)
plt.title("Histogram Plot")
plt.xlabel("Value")
plt.ylabel("Frequency")

print("The Mean of the data is :",np.mean(xValuesnp))
print("The Variance of the data is :",np.var(xValuesnp,dtype=np.float64))