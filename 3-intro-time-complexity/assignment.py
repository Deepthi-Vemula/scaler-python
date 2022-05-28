# Q1. CHOOSE4
# What does it mean when we say that an algorithm X is asymptotically more efficient than Y?
# A. X will always be a better choice for large inputs
#
#
# Q2. CHOOSE3
# In a competition, four different functions are observed.
# All the functions use a single for loop and within the for loop,
# same set of statements are executed.
#
# Consider the following for loops:
#     A) for(i = 0; i < n; i++)
#
#     B) for(i = 0; i < n; i += 2)
#
#     C) for(i = 1; i < n; i *= 2)
#
#     D) for(i = n; i > -1; i /= 2)
#
#     If n is the size of input(positive), which function is the most efficient?
#     In other words, which loop completes the fastest.
# A. C - log(N) time complexity
#
# Q3. Choose2
#
# Which of the given options provides the increasing order of complexity of functions
# f1, f2, f3 and f4:
#     f1(n) = 2^n
#
#     f2(n) = n^(3/2) = n*sqrt(n)
#
#     f3(n) = nLogn
#
#     f4(n) = n^(Logn)
# nlogn < n*sqrt(n) < n^log(n) < 2^n
#     f3 < f2 < f4 < f1
#
# Q4. CHOOSE1
# Which of the following is not bounded by O(n^2)?
#     (15^10) * n + 12099  = O(n)
#     n^1.98 - O(n^1.98) ~ O(n^2)
#     n^3 / (sqrt(n))  = n^(3-1/2) = O(n^2.5)
#     (2^20) * n = O(n)
#
#
# Q5. If condition evaluation
#     What will be the value of y after the execution of the following code?
#     var x;
#     var y = 10;
#
#     if (x) {
#     y = y + x;
#     }
#     console.log(y);
#     Note: in some languages, var is auto-initialized to 0
#     case 1 : var auto-init to 0 ans = 10
#     case 2 : x = undefined , y = undefined
#     generally we take the value as undefined unless explicitly mentioned
#     so, y = undefined
#
# Q6. LOOP_CMPL
#     What is the time, space complexity of following code :
#     int a = 0, b = 0;
#     for (i = 0; i < N; i++) {
#         a = a + rand();
#     }
#     for (j = 0; j < M; j++) {
#     b = b + rand();
#     }
#     ans : O(N + M) time, O(1) space
#
# Q7. LOOP_CMPL2
#     What is the time complexity of the following code :
#     int i, j, k = 0;
#     for (i  = n/2; i <= n; i++) {
#     for (j = 2; j <= n; j = j * 2) {
#     k = k + n/2;
#     }
#     }
#     ans: &Theta;(nLogn)
#
# Q8. NESTED_CMPL
#     What is the time, space complexity of following code :
#
#
#    Ans:  O(N * N) time, O(1) space
#
#
# Q9. NESTED_CMPL2
#     What is the time complexity of the following code :
#     Ans: O(N*N)
#
# Q10. NESTED_CMPL3
#     What is time complexity of following code :
#     Ans: O(N * log N)
#
