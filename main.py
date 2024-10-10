from datetime import date, datetime
steps=open("steps.txt",'r')
count=0
f = open("SMITH_AVG.txt".txt", "w")
f.writelines(["Average Steps Per Month\n", "Month  Average\n", "----------------\n"])
f.close()
for i in range(1,13):
    if ((i == 1) or (i == 3) or (i == 5) or (i == 7) or (i == 8) or (i == 10) or (i ==12)):
        n = 31
    elif (i == 2):
        n = 28
    elif ((i == 4) or (i == 6) or (i ==9) or (i == 11)):
        n = 30
    count=0
    total=0
    while(count<n):
        num_steps=int(steps.readline())
        total+=num_steps
        count+=1
#    print lines
    f = open('GEDDES_AVG.txt','a')
    f.write("Month ")
    f.write(str(i))
    f.write('=')
    f.write(str(total) + '\n')
    f.close()
steps.close()
