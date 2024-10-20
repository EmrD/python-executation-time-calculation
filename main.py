import timeit

start_time = timeit.default_timer()

list = []

# Example usage. In my case the result was 0.006873699952848256 seconds.
for i in range(10001):
    list.append(i)

for i in range(100001):
    if i == 50087654321:
        print("Found")
        break

stop_time = timeit.default_timer()
execution_time = stop_time - start_time

print("Program executed in " + str(execution_time) + " seconds")