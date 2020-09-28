import json
import re

f = open("document.csv", "r")
all_data = f.read()
f.close()

cve_lines = all_data.strip().split("\n")
# print(cve_lines)

def get_cvss(version):
    tmp = None
    score = None
    for line in cve_lines:
        if line[:3] == version:
            tmp = line.split(",")

    if tmp:
        score = 0.0
        for i in range(1,len(tmp)):
            score += float(tmp[i])
    
    return score


output = {}
with open('1.json') as f:
    for line in f:
        j_content = json.loads(line)
        match = re.search(r"OpenSSH_(\d\.\d)(.*?)[ \\n]", j_content['banner'])
        if match:
            try:
                cvss = round(get_cvss(match.group(1)),2)
                key = j_content['geo']['c']

                if key in output:
                    output[key]['cvss'] += cvss
                    output[key]['num'] += 1
                else:
                    output[key] = {"cvss": cvss, "num": 1}

                # tmp = {j_content['ip']: [match.group(1)] , j_content['geo']['c'], 'empty'}
                # output.append(tmp) #update rates
            
            except Exception:
                continue

f = open("1out.csv", "w")
for key in output:
    f.write(key)
    f.write(",")
    f.write( str(round((output[key]['cvss'] / output[key]['num']), 2)) )
    f.write(",")
    f.write( str(output[key]['num']) )
    f.write("\n")

f.close()