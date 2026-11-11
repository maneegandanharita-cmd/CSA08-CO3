calls = [
    "seeds not received seeds delayed",
    "fertiliser price high",
    "seeds price high subsidy not received"
]
STOP = {"not", "high"}

def frequencies(texts, stop):
    counts = {}
    for text in texts:
        for word in text.lower().split():
            if word not in stop:
                counts[word] = counts.get(word, 0) + 1
    return counts

def top(counts, k):
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:k]

print("Frequencies:", frequencies(calls, STOP))
print("Top 3:", top(frequencies(calls, STOP), 3))

complaints = [
    ("Chennai", "seeds delayed"),
    ("Madurai", "fertiliser price high"),
    ("Chennai", "subsidy not received")
]
by_district = {}
for district, complaint in complaints:
    by_district.setdefault(district, []).append(complaint)
print("By district:", by_district)
