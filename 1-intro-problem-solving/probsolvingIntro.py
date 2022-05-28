# Q1:
# You are having a Helmet of Level 1 and a VEST, what will be the damage?
# ans: 405

# Q2:
# You have to follow the following steps to find the sqrt of an integer N.
#
# Consider L = 1, R = N, and cnt = 0
#
# STEP 1: MID = (floor)(L+R)/2 and cnt += 1
#
# STEP 2: if ((MID * MID) == N), then go to STEP 5 else go to STEP 3.
#
# STEP 3: if ((MID * MID) < N), then L = MID+1 and go to STEP 1 else STEP 4.
#
# STEP 4: if ((MID * MID) > N), then R = MID - 1 and go to STEP 1.
#
# STEP 5: PRINT MID.
#
# If the value of N is 36, what will be the value of cnt?
# Ans:
# 1-36 mid= 18 cnt = 1 18*18>N
# 1-17 mid = 9 cnt = 2 9*9>N
# 1-8 mid = 4 cnt = 3 4*4 <n
# 5-6 mid = 5 cnt = 4 5*5<n
# 6 mid = 6 cnt =5 6*6 == n
# cnt = 5


#Q3:
# If your computer program is using this decision tree,
# how many questions, on average,
# will the computer program need to ask and answer in order to distinguish a random face?
# ans : 2

