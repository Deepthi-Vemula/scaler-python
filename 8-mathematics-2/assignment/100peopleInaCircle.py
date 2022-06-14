# Q2. 100 People in a Circle
# One hundred people are standing in a circle in an order 1 to 100.
#
# No.1 has a sword. He kills the next person (i.e., no. 2) and gives the sword to the next (i.e., no. 3).
# All person does the same until only one survives.
#
# Which number survives at last?
#
# Answer is an integer. Just put the number without any decimal places if it's an integer.
# If the answer is Infinity, output Infinity.
#

# Answer: greatest power of 2 close to 100 which is lower than 100 = pow(2,6) = 64
# 2*(100-64) + 1 = 73
# hence, answer = 73
