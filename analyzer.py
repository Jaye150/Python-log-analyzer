counts = {}
with open("sample-auth.log") as f:
    for line in f:
        line=line.strip()
        if "FAILED" in line:
            word=line.split()
            ip=word[4].split("=")
            if ip[1] in counts:
                counts[ip[1]] = counts[ip[1]] + 1
            else:
                counts[ip[1]] = 1
threshold = 5
with open("report.txt", "w") as report:
    for address, total in counts.items():
        if total >= threshold:
            print("ALERT:", address, total, "failed logins")
            print("ALERT:", address, total, "failed logins", file=report)
