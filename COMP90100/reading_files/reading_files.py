# fp = open("COMP90100/incident_report_brute_force_attack.txt")
# content = fp.read()
# fp.close()

# print(content)

# print("--------")
# fp = open("COMP90100/incident_report_initial_triage.txt")
# lineno = 1
# for line in fp.readlines():
#     print(f"{lineno}: {line}", end='')
#     lineno += 1
# fp.close()

# print("--------")

# fp = open("COMP90100/incident_report_mitigation_strategies.txt")
# lineno = 1
# for line in fp:  # note no readlines()
#     print(f"{lineno}: {line}", end='')
#     lineno += 1
# fp.close()

# print("--------")

# fp = open("COMP90100/incident_report_initial_triage.txt")
# line = fp.readline()
# print(line, end='')
# line = fp.readline()
# print(line, end='')
# line = fp.readline()
# print(line, end='')
# fp.close()

# Read from the original file
fp = open("COMP90100/quotes.txt")
content = fp.read()
fp.close()

# Create a copy by writing content to keep original file
fp = open("COMP90100/quotes2.txt", "w")
fp.write(content)
fp.close()

# Append content to a copy file
fp = open("COMP90100/quotes2.txt", "a")
fp.write("\n\n- Edsger Dijkstra")
fp.close()
fp = open("COMP90100/quotes2.txt", "r")
print(fp.read())
fp.close()