# Executation Time Calculation of Python file in Python

This Python file uses the following packages to calculate the time:

- timeit

## Example Usage
To test, I wrote a code like this; 

```
for i in range(10001):
    list.append(i)

for i in range(100001):
    if i == 50087654321:
        print("Found")
        break
````

and the result was 0.006873699952848256 seconds.