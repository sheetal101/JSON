import json

filename = 'data.txt'
  
dict1 = {}
  
with open(filename) as fy:
  
    for line in fy:
  
        # reads each line and trims of extra the spaces 
        # and gives only the valid words
        i, j = line.strip().split(None, 1)
        print(i)
        print(j)    
  
        dict1[i] = j.strip()

out_file = open("test1.json", "w")
json.dump(dict1, out_file, indent = 4)
out_file.close()
