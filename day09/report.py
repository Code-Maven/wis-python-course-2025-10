import re

filename = "subjects.txt"
with open(filename) as fh:
    for line in fh:
        #print(line)
        #if "day" in line.lower():
        # if "Day" in line or "day" in line:
        #     print(line)
        parts = line.split("\t")
        #print(parts)
        subject = parts[2]
        print(subject)
        match = re.search(r"day\s*[0-9]+", subject, re.IGNORECASE)
        if match:
            print(match.group(0))

r"^([0-9]+)\s*$"
