
import os
def read(i):
    f = open("d:/tmp/"+i+".txt")
    lines = f.readlines()
    print(lines)
    f.close()
    return len(lines)

def write():
    for i in range(20):
        with open('d:/tmp/'+str(i) + ".txt",'w') as f:
            for j in range(10):
                f.write("line" + str(j) + "\n")



def show():
    files = os.listdir("d:/tmp");
    for file in files:
        if file.endswith(".txt"):
            print file
write();

# read();
# show()