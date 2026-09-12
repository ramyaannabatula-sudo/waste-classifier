count = 1
while count <= 5:
    print("checking waste",count)
    count = count + 1


for i in range(1,11):
    if i == 6:
        break
    print("checking waste",i)


#for - repeat a fixed no. of times
#while - repeat while a condition is true
#break - stop the loop completely
#continue - skips one iteration but keeps the loop going



for i in range(1,6):
    if i == 3:
        continue
    print("checking waste",i)

for i in range(1,11):
    if i == 5:
        continue
    print("checking waste",i)