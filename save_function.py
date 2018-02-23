#def savefile ():
sections = ("Number of loci", "Sampling Vector", "Initial deme sizes", "Initial migration matrix","Time of change", "Deme sizes")


#comes from the main document
matrix = ["1","2","3"],["4","5","6"],["9","2","3"],[("0. 0. 0. 0."),("0. 0. 0. 0."),("0. 0. 0. 0.")],["4","5","6"],["1","2","3"]


name = []
for i in range(0,6):
    name.append("final_doc"+str(i)+".txt")
    
for n in range(0,3):
    finaldoc = open(name[n],"w")
    for i in range(0,6):
        finaldoc.write(sections[i]+"\n")
        finaldoc.write(matrix[i][n]+"\n\n")

finaldoc.close()
