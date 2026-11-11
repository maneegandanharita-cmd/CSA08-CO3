readings = [4, 7, 55, -60, 1, 9, 6, 51, 3]
valid = [c for c in readings if -50 <= c <= 50]
fahrenheit = [round(c * 9/5 + 32, 2) for c in valid]
alarms = [(i+1, c) for i, c in enumerate(readings)
          if -50 <= c <= 50 and not (2 <= c <= 8)]
print("Original:", readings)
print("Valid Celsius:", valid)
print("Fahrenheit:", fahrenheit)
print("Alarm minutes (minute, Celsius):", alarms)
loop_valid = []
for c in readings:
    if -50 <= c <= 50:
        loop_valid.append(c)
print("Loop matches comprehension:", loop_valid == valid)
filtered = list(filter(lambda c: -50 <= c <= 50, readings))
print("Filter matches comprehension:", filtered == valid)
