# Q1. Color of the last ball
# You have 20 blue balls and 14 red balls in a bag. You put your hand in and remove 2 at a time.
#
# If they’re of the same color, you add a blue ball to the bag.
# If they’re of different colors, you add a red ball to the bag.
# ( Assume you have a big supply of blue & red balls for this purpose).
#
# Note: When you take the two balls out, you don’t put them back in, so the number of balls in the bag keeps decreasing.
#
# What will be the color of the last ball left in the bag?

# here, there are 3 cases
#     we pick - 2B , 2R, B+R
#     a. if we pick 2B continuously, we are left with all red balls = for 2R -> we get 1B ball - finally we will be left with a blue ball
#         in all scenarios - we are left with a red balls -> then picking 2Red balls each time - we have one last blue ball