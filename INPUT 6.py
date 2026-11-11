timetable = {
 "12601": {"name":"Chennai Express", "stops":[("Chennai","06:00","06:15"),("Katpadi","08:00","08:05"),("Bengaluru","11:00","11:10")], "days":{"Mon","Wed","Fri"}},
 "12602": {"name":"Kaveri Express", "stops":[("Chennai","07:00","07:20"),("Katpadi","09:10","09:15"),("Mysuru","13:00","13:10")], "days":{"Tue","Thu","Sat"}},
 "12603": {"name":"Coastal Express", "stops":[("Chennai","08:00","08:10"),("Villupuram","10:00","10:05"),("Trichy","13:00","13:10")], "days":{"Mon","Tue","Wed","Thu","Fri","Sat","Sun"}},
 "12604": {"name":"Hill Express", "stops":[("Bengaluru","05:00","05:10"),("Katpadi","08:30","08:35"),("Chennai","11:00","11:15")], "days":{"Sun"}},
 "12605": {"name":"Southern Express", "stops":[("Chennai","09:00","09:10"),("Katpadi","11:00","11:05"),("Coimbatore","16:00","16:10")], "days":{"Mon","Thu","Sat"}}
}
station, day = "Katpadi", "Mon"
matches = []
for number, details in timetable.items():
    if day in details["days"]:
        for stop, arrival, departure in details["stops"]:
            if stop == station:
                matches.append((departure, number, details["name"], arrival))
matches.sort(key=lambda item: item[0])
print("Trains stopping at", station, "on", day)
for departure, number, name, arrival in matches:
    print(number, name, "Arrival:", arrival, "Departure:", departure)
print("Total trains:", len(matches))
