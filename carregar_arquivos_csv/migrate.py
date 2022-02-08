from os.path import exists
import time


def lerDados(id=1, count = 0):
  file1 = open(f"dados_{id}.csv", 'r')
  print(f"============= lendo arquivo dados_{id}.csv ============= ")
  time.sleep(2)
  
  while True:
    count += 1
    line = file1.readline()
    if not line:
      break
    print("Line {}: {}".format(count, line.strip()))
  file1.close()

  if exists(f"dados_{(id + 1)}.csv"):
    lerDados(id+1, count)


lerDados()