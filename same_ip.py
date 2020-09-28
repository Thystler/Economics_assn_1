import json
import re

outF = open("outfile.txt","w")

output = {}
with open('6.json') as f:
    for line in f:
        j_content = json.loads(line)
        match = re.search(r"OpenSSH_(.*?)[ \\n]", j_content['banner'])
        if match:
            try:
                output[j_content['ip']] = {"ver": [match.group(1)], "geo": j_content['geo']['c'], "updated": False}

                # tmp = {j_content['ip']: [match.group(1)] , j_content['geo']['c'], 'empty'}
                # output.append(tmp) #update rates
            
            except Exception:
                continue

print("1 done")

with open('11.json') as f:

    for line in f:
        j_content = json.loads(line)

        match = re.search(r"OpenSSH_(.*?)[ \\n]", j_content['banner'])
        if match:
            try:
                output[j_content['ip']]['ver'].append(match.group(1))
            except Exception:
                continue    

print("2 done")

for ip in list(output.keys()):
    if len(output[ip]["ver"]) < 2:
        del output[ip]

# coutlef = open('outfile1.txt','w')
# coutlef.write(str(output))
# coutlef.close()

for ip in (output):
    if output[ip]["ver"][0] != output[ip]["ver"][1]:
        output[ip]["updated"] = True

country_updated = {}
country_unupdated = {}

# updated = 0
# unupdated = 0
# total = 0
# for i in output:
#     if output[i]["updated"] == True:
#         updated += 1
#     else:
#         unupdated += 1
#     total += 1

# print('updated', updated)
# print('unupdated',unupdated)
# print('total',total)

for i in output:
    if output[i]["updated"] == True:
        if output[i]["geo"] not in country_updated:
            country_updated[output[i]["geo"]] = 1

        else:
            country_updated[output[i]["geo"]] += 1

    else:
        if output[i]["geo"] not in country_unupdated:
            country_unupdated[output[i]["geo"]] = 1

        else:
            country_unupdated[output[i]["geo"]] += 1



import csv

with open('6-11.csv', 'w', newline='') as csvfile:
    fieldnames = ['Country', 'updated','unupdated']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in country_unupdated:
        if i in country_updated:
            writer.writerow({'Country': i, 'updated': country_updated[i],'unupdated': country_unupdated[i]})
        else:
            writer.writerow({'Country': i, 'updated': 0,'unupdated': country_unupdated[i]})

coutlef = open('outfile.txt','w')

for each in output:
    tmp = (each, output[each])
    coutlef.write(str(tmp) + "\n")
coutlef.close()