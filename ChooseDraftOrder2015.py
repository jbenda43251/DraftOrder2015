import random
nameDict = {}
nameDict['Thrall'] = 0
nameDict["C'Thun"] = 0
nameDict['Valeera Sanguinar'] = 0
nameDict["Medivh"] = 0
nameDict['King Mrgl Mrgl'] = 0
nameDict['Lady Sylvanas'] = 0
nameDict['Uther'] = 0
nameDict['Broxigar the Red'] = 0
ownerDict = {}
ownerDict['Thrall'] = 'Shannon'
ownerDict["C'Thun"] = 'Jeff'
ownerDict['Valeera Sanguinar'] = 'Travis'
ownerDict["Medivh"] = 'Joe'
ownerDict['King Mrgl Mrgl'] = 'Winnie'
ownerDict['Lady Sylvanas'] = 'Caitlin'
ownerDict['Uther'] = 'Benders'
ownerDict['Broxigar the Red'] = 'Checkers'
valueDict = {}
names = ['Thrall', "C'Thun", 'Valeera Sanguinar',"Medivh",
         'King Mrgl Mrgl', 'Lady Sylvanas', 'Uther', 'Broxigar the Red']

for i in range(2500):
    random.shuffle(names, random.random)
    for j in range(8):
        nameDict[names[j]] += j
values = []
for i in range(8):
    valueDict[nameDict[names[i]]] = names[i]
    values.append(nameDict[names[i]])
    print names[i] + ' total:' + str(nameDict[names[i]])
print '-------------------------'
values.sort()
for i in range(8):
    print str(i+1) + '. ' + ownerDict[valueDict[values[i]]] + '('+ valueDict[values[i]]+ ')'
