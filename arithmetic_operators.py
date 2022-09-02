# Addition
print(20+30)

# Subtraction
print(50 - 20)

# Multiplication
print(10 * 10)

# Division
print(100 / 5)

# Exponentiation
print(6**2)
print(5**2 + 20)

# Examples

# 1. How many seconds are there in 42 minutes 42 seconds?
print(42*60 + 42)

# 2. How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile
print(10/1.61)

# 3. If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per mile in minutes and seconds)? What is your average speed in miles per hour?
avg_pace = (10/1.61)/(42*60 + 42)
print(avg_pace)

avg_speed_hour = (10/1.61)/((42*60 + 42)/3600)
print(avg_speed_hour)
