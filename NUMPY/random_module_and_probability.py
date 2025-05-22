import numpy as np

# normally random module is used
# using numpy for random generation

print(np.random.random()) # will generate a random number

arr = np.random.random(10) # will generate 10 random floats b/w 0 to 1
print(arr)

# random int no.s using SystemRandom()
from random import SystemRandom
sr = SystemRandom()
num = sr.randint(1,10)

# # automatic pass generator
# length = int(input("Length: "))
# vaild_chars = input("Valid Charaters (X for default valid list): ")
# if vaild_chars == "X" : 
#     vaild_chars = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890'
# cnt = 0
# password = ''
# while cnt < length :
#     num = sr.randint(0,61)
#     password += vaild_chars[num]
#     cnt +=1
# print(password)


# using numpy module
random_num = np.random.randint(1,7,size=10) # will generate 10 int samples from 1 to 6 (7 excluded)
print(random_num)

print(np.random.randint(1,7,size = (3,6))) # generate an arr of shape (3,6)

# random choices
import random
choices = ['hello','hi','bye']
print(random.choice(choices))  # chooses a random choice from choices

# using numpy choice(list,shape,replace) replace if true : string can repeat
print(np.random.choice(choices,size=(3,2)))  



# WEIGHTED RANDOM CHOICES

    # making cumulative weights
wts = [0.2,0.5,0.3]
cum_wts = [0] + list(np.cumsum(wts))   #  -> CDF
print(cum_wts) # [0, np.float64(0.2), np.float64(0.7), np.float64(1.0)]

# working
objects = ['apple','banana','pear']
weights = [1,3,1]
wts = np.array(weights,dtype=np.float32)  # making wts float
wts = wts/wts.sum()  # turning wts into probabilities
wts = np.cumsum(wts)  # getting the cdf
num = np.random.random() 
for i in range(len(wts)) :
    if num < wts[i] :  # if the random num is less than the wt then only print it
        print(objects[i])
        break


# USING WEIGHTED CHOICE IN NUMPY

# np.choice(object_arr, shape, replace, (p) prob_arr/weights)
objects = ["scientist","philosopher","engineer","priest","programmer"]
prob = [0.2, 0.05, 0.3, 0.15, 0.3]

print(np.random.choice(objects, p=prob)) # direct implementation of weighted prob


candies = ["red", "green", "blue", "yellow", "black", "white", "pink", "orange"]
weights = [ 1/24, 1/6, 1/6, 1/12, 1/12, 1/24, 1/8, 7/24]

# QUES given the candies and their wts, calculate the probability that in each trial
# you pick 3 colors out of which atleast 1 is orange such that n trials are conducted
n = int(input("No. of trials: "))
or_cnt = 0
for i in range(n):
    if "orange" in np.random.choice(candies,(3,),replace=False,p=weights):
        or_cnt += 1
print("Prob = ",or_cnt/n)
