import os 
path = "/"
dir_list = os.listdir(path) 
print("Files and directories in '", path, "' :") 
print(dir_list) 
print(len(dir_list))
rj=""
for i in range(len(dir_list)):
  change= dir_list[i].replace(".html","")
  #print(change)
  rj= change

print(rj) 
