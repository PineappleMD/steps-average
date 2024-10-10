def main():
  month = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
  days = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
  file = open('steps.txt', 'r')
  f = open("membreno_avg.txt", "w")
  f.writelines(["Average Steps Taken Per Month\n", "Month      Average\n", "-------------------------\n"])
  f.close()
  for x in range(12):
    total = 0
    average = 0
    for y in range(12):
      file = open('steps.txt', 'r')
      steps = int(file.readline())
      total += steps
      average = total/ days[x]
    f = open('membreno_avg.txt', 'a')
    f.write(month[x])
    f.write('=')
    f.write(str(average) + '\n')
    f.close()
    file.close()

    
main()
