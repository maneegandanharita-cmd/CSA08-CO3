import time

contacts = [
 {"name":"Dr. Ravi", "phone":"+91 98400 12345", "email":"ravi@mail.com"},
 {"name":"Ravi Kumar", "phone":"9840012345", "email":"r.kumar@mail.com"},
 {"name":"Anu", "phone":"9876543210", "email":"anu@mail.com"},
 {"name":"Ravi", "phone":"091 98400-12345", "email":"ravi@mail.com"}
]

def normalise_phone(phone):
    digits = "".join(ch for ch in phone if ch.isdigit())
    if digits.startswith("91") and len(digits) == 12:
        digits = digits[2:]
    if digits.startswith("0") and len(digits) == 11:
        digits = digits[1:]
    return digits

def merge_contacts(records):
    merged = {}
    for contact in records:
        key = normalise_phone(contact.get("phone", ""))
        if not key:
            continue
        if key not in merged:
            merged[key] = {"names": set(), "phones": set(), "emails": set()}
        if contact.get("name"):
            merged[key]["names"].add(contact["name"])
        if contact.get("phone"):
            merged[key]["phones"].add(contact["phone"])
        if contact.get("email"):
            merged[key]["emails"].add(contact["email"])
    return merged

start = time.perf_counter()
result = merge_contacts(contacts)
elapsed = time.perf_counter() - start
for number, details in sorted(result.items()):
    print("Normalised number:", number)
    print("Names:", sorted(details["names"]))
    print("Phones:", sorted(details["phones"]))
    print("Emails:", sorted(details["emails"]))
print("Unique contacts:", len(result))
print("Time:", round(elapsed, 6), "seconds")
