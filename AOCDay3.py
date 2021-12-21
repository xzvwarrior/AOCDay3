
with open("FullList.txt") as f:
    Testlist = f.readlines()

firstbit = []
secondbit = []
thirdbit = []
fourthbit = []
fifthbit = []
sixthbit = []
seventhbit = []

for x in Testlist:
    firstbit.append(int((x[:1])))
    secondbit.append(int((x[1:2])))
    thirdbit.append(int((x[2:3])))
    fourthbit.append(int((x[3:4])))
    fifthbit.append(int((x[4:5])))
    sixthbit.append(int((x[5:6])))
    seventhbit.append(int((x[6:7])))

counter = 0
counter2 = 0

#for x in bits I would want to call the function and pass it the bit we're on. 
for x in firstbit:  
    if firstbit[x] > 0:
        counter += 1
    else:
        counter2 += 1

Gamma = []
Epsilon = []
counter = 0
counter2 = 0
if counter > counter2:
    Gamma.append(1)
    Epsilon.append(0)
else:
    Gamma.append(0)
    Epsilon.append(1)
counter = 0
counter2 = 0

for x in secondbit:
    if int(secondbit[x]) > 0:
        counter += 1
    else:
        counter2 += 1

if counter > counter2:
    Gamma.append(1)
    Epsilon.append(0)
else:
    Gamma.append(0)
    Epsilon.append(1)
counter = 0
counter2 = 0

for x in thirdbit:
    if thirdbit[x] > 0:
        counter += 1
    else:
        counter2 += 1

if counter > counter2:
    Gamma.append(1)
    Epsilon.append(0)
else:
    Gamma.append(0)
    Epsilon.append(1)
counter = 0
counter2 = 0

for x in fourthbit:
    if fourthbit[x] > 0:
        counter += 1
    else:
        counter2 += 1

if counter > counter2:
    Gamma.append(1)
    Epsilon.append(0)
else:
    Gamma.append(0)
    Epsilon.append(1)
counter = 0
counter2 = 0

for x in fifthbit:
    if fifthbit[x] > 0:
        counter += 1
    else:
        counter2 += 1

if counter > counter2:
    Gamma.append(1)
    Epsilon.append(0)
else:
    Gamma.append(0)
    Epsilon.append(1)
counter = 0
counter2 = 0

for x in sixthbit:
    if sixthbit[x] > 0:
        counter += 1
    else:
        counter2 += 1

if counter > counter2:
    Gamma.append(1)
    Epsilon.append(0)
else:
    Gamma.append(0)
    Epsilon.append(1)
counter = 0
counter2 = 0

for x in seventhbit:
    if seventhbit[x] > 0:
        counter += 1
    else:
        counter2 += 1

if counter > counter2:
    Gamma.append(1)
    Epsilon.append(0)
else:
    Gamma.append(0)
    Epsilon.append(1)
counter = 0
counter2 = 0

print(Gamma)
print(Epsilon)

string = ''
for x in Gamma:
    string += str(x)
        
string2 = ''
for x in Epsilon:
    string2 += str(x)

print(int(string,2))
print(int(string2,2))