import json

outF = open("outfile.txt","w")

output = []
with open('1.json') as f:
    for line in f:
        j_content = json.loads(line)
        output.append(j_content['ip'])

print(len(output))
output = set(output)
print(len(output))

for i in range(11,12,1):
    compare = []
    with open('{0}.json'.format(i)) as f:
        print('{0}.json'.format(i))
        #prepare the set
        for line in f:
            compare.append(json.loads(line)['ip'])
        
        #check weither the ip is in or not
        print("removing")
        output = set(output) & set(compare)
        print(len(output))



