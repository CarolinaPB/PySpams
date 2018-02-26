def save_file(test):
    sections = ("Number of loci", "Sampling Vector", "Initial deme sizes", "Initial migration matrix","Time of change", "Deme sizes")

    name = []
    for i in range(0,6):
        name.append("final_doc"+str(i)+".txt")
        
    for n in range(0,3):
        finaldoc = open(name[n],"w")
        for i in range(0,6):
            finaldoc.write(sections[i]+"\n")
            finaldoc.write(test[i,n]+"\n\n")

    finaldoc.close()
    
