import random
import time

readings = [0, 12, 5, 8, 0, 20, 15, 3, 0, 7, 10, 4, 6, 0, 18, 2, 1, 0, 9, 11, 5]
weekly = [sum(readings[i:i+7]) for i in range(0, len(readings), 7)]
wettest = max(readings)
driest = min(readings)
moving = []
running = sum(readings[:7])
if len(readings) >= 7:
    moving.append(round(running / 7, 2))
    for i in range(7, len(readings)):
        running += readings[i] - readings[i-7]
        if i >= 6:
            moving.append(round(running / 7, 2))
dry_days = [i+1 for i, value in enumerate(readings) if value == 0]

print("Weekly totals:", weekly)
print("Wettest day:", readings.index(wettest)+1, "Rainfall:", wettest)
print("Driest day:", readings.index(driest)+1, "Rainfall:", driest)
print("7-day moving averages:", moving)
print("Dry days:", dry_days)
print("Slice readings[7:14]:", readings[7:14])
print("Slice readings[-7:]:", readings[-7:])
print("Slice readings[::7]:", readings[::7])

def naive_avg(a):
    return [sum(a[i:i+7])/7 for i in range(len(a)-6)]
def running_avg(a):
    if len(a) < 7: return []
    total = sum(a[:7]); result = [total/7]
    for i in range(7, len(a)):
        total += a[i] - a[i-7]
        result.append(total/7)
    return result

for n in (365, 36500, 365000):
    data = [random.randint(0, 30) for _ in range(n)]
    t1=time.perf_counter(); naive_avg(data); naive=time.perf_counter()-t1
    t1=time.perf_counter(); running_avg(data); fast=time.perf_counter()-t1
    print("n =", n, "naive =", round(naive, 5), "running =", round(fast, 5))
print("Empty list:", running_avg([]))
print("Short list:", running_avg([1, 2, 3]))
