
1. One of the following 10 statements generates an error. Which one? (Your answer should be a number between 1 and 10.)
```
x = [1,"abcd",2,"efgh",[3,4]]  # Statement 1
y = x[0:50]                    # Statement 2
z = y                          # Statement 3
w = x                          # Statement 4
x[1] = x[1][0:3] + 'd'         # Statement 5
y[2] = 4                       # Statement 6
z[0] = 0                       # Statement 7
x[1][1:2] = 'yzw'              # Statement 8
w[4][0] = 1000                 # Statement 9
a = (x[4][1] == 4)             # Statement 10
```


2. Consider the following lines of Python code.
```
x = ['a',42,'b',377]
w = x[1:]
y = x
u = w
w = w[0:]
w[0] = 53
x[1] = 47

```
3. Which of the following is correct?
 
 
 ```
 x[1] == 47, y[1] == 47, w[0] == 53, u[0] == 42
 x[1] == 47, y[1] == 47, w[0] == 53, u[0] == 53
 x[1] == 47, y[1] == 42, w[0] == 53, u[0] == 53
 x[1] == 47, y[1] == 42, w[0] == 53, u[0] == 53
```

4. What is the value of second after executing the following lines?
```
first = "wombat"
second = ""
for i in range(len(first),0,-1):
  second = first[i-1] + second
```

5. What is the value of list1 after the following lines are executed?
def mystery(l):
  l = l[2:5]
  return()

list1 = [7,82,44,23,11]
mystery(list1)