import os

classes = sorted(os.listdir("MIRO/"))

indices = ['035', '115', '047', '127', '039', '119', '043', '123', '021', '133', '029', '141', '049', '097', '057', '105', '068', '070', '078', '076'];

for c in classes:
    os.system("mkdir -p MIRO_case2/"+c)
    os.chdir("MIRO_case2/"+c)
    for i in range(1,11):
        for j in range(1,21):
            src = "../../MIRO/"+c+"/"+c+"_"+str(i)+"_"+indices[j-1]+".png"
            dst = c+"_"+str(i)+"_"+str(j).zfill(3)+".png"
            os.system("ln -s "+src+" "+dst)
    os.chdir("../..")
