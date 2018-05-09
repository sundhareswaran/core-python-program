import random
print"choice([1,2,3,4,5]):",random.choice([1,2,3,4,5])
print"choice('python'):",random.choice('python')
print"random:",random.random()
random.seed(9)
print"seed 9:",random.random()
list = [20, 16, 10, 5];
random.shuffle(list)
print "Reshuffled list : ",  list
random.shuffle(list)
print "Reshuffled list : ",  list
random.uniform(5,10)
print"random float uniform(5,10):",random.uniform(5,10)
print"random float uniform(7,14):",random.uniform(7,14)


