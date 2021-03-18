

import math


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from scipy.stats import norm
from scipy.stats import binom


#function to calculate factorial
def fact_func(a):
  ans = 1
  for x in range(1 , a + 1):
    ans = ans * x
  return ans

#function to calculate binomial coefficient
def ncr(n , r):
  ans = fact_func(n) / (fact_func(r) * fact_func(n - r))
  return ans

#function to calculate the probability 
def probab_func(n , p , q , a , b):
  sum = 0
  for x in range(a , b + 1):
    sum = sum + ( ncr(n , x) )* ( pow(p , x) ) * ( pow(q , n - x) )
  return sum

n = 4
p = 1 / 10
q = 9 / 10
case_1 = probab_func(n , p , q , 0 , 0)

print("The Theoritical probability that none of the ball is marked with the digit : " , probab_func(n , p , q , 0 , 0))

#Simulations

k = 1000000
sample_space = np.random.binomial(n,p,k)
#print("Some number this is ", sample_space)
count = 0
for i in sample_space:
  if i == 0:
    count = count + 1

prob = count / k
case_1_sim = prob
print("The Simulated probability that none of the ball is marked with the digit : ", prob)



#plotting

cases = ["X=0"]

probab_theo = [case_1]
probab_sim = [case_1_sim]

x = np.arange(len(cases))
plt.bar(x + 0.00, probab_theo, color = 'b', width = 0.25, label = 'Theoretical')
plt.bar(x + 0.25, probab_sim, color = 'g', width = 0.25, label = 'Sim')
#plt.xlabel('X=0')
plt.ylabel('Probability')
plt.xticks(x  + 0.25/2,['X=0'])
plt.legend()
plt.show()
