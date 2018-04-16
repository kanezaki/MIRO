import os

classes = sorted(os.listdir("MIRO/"))

for c in classes:
    os.system("mkdir -p MIRO_case1/"+c)
    os.chdir("MIRO_case1/"+c)
    for i in range(1,11):
        for j in range(1,17):
            src = "../../MIRO/"+c+"/"+c+"_"+str(i)+"_"+str(j+64).zfill(3)+".png"
            dst = c+"_"+str(i)+"_"+str(j).zfill(3)+".png"
            os.system("ln -s "+src+" "+dst)
    os.chdir("../..")
