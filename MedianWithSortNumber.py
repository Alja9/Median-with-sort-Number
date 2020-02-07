import statistics

items = []
while(True):
       inp = int(input())
       if inp == 0:
              print(items)
              print("Median with sort number: ")
              print(statistics.median(items))
              break
       items.append(inp)
       print(items)
