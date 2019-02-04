# Assignment 
1. What is the value of f(255) for the function below?
def f(x):
    d=0;
    while(x>=1)
        (x,d) =(x/4,d+1)
    return(d);

Ans:

2. What is h(28) - h(27), given the definition of h below?
def h(n):
    s = 0
    for i in range(1,n):
        if n%i == 0:
           s = s+i
    return(s)

Ans:

3. For what value of n would g(47,n) return 5?
def g(m,n):
    res = 0
    while m >= n:
        (res,m) = (res+1,m-n)
    return(res)

Ans: 5

4. Consider the following function f:

def mys(m):
  if m == 0:
    return(1)
  else:
    return(m*mys(m-1))

Which of the following is correct?
* The function always terminates with mys(n) = factorial of n
* The function always terminates with mys(n) = 1+2+...+n
* The function terminates for non­negative n with mys(n) = factorial of n
* The function terminates for non­negative n with mys(n) = 1+2+...+n

Ans: C