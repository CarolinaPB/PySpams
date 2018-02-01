output_file = open("input_test.txt","w")

###Number of loci
loci = raw_input("# Number of loci \n")
###Sampling vector
samp_vector = list(raw_input("# Sampling vector \n"))
vector_res=''
for n in samp_vector:
	vector_res=vector_res + n + " "
print vector_res
print "\n"
###Initial deme sizes
inideme_size = raw_input("# Initial deme sizes \n")
inideme_res=''
for i in inideme_size:
	inideme_res= inideme_res +i +" "
print inideme_res
###Initial migration matrix

output_file.write("Sampling vector \n")
output_file.write(vector_res)
output_file.write("\n")



output_file.close()



#test= (loci, samp_vector)
#print test

#for i in test:
	#print i

#input_file.write(loci)
#input_file.write(samp_vector)








#loci = int(raw_input("# Number of loci \n"))

#info_doc = ["raw_input1", "raw_input2"]
#file.write(info_doc)

#input_file = open("input_test.txt","w")
#input_file.write(loci)

#input_file.close()

