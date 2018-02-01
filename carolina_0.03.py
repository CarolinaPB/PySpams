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



output_file.write("# Number of loci \n")
output_file.write(loci)
output_file.write("\n")
output_file.write("# Sampling vector \n")
output_file.write(vector_res)
output_file.write("\n")
output_file.write("# Initial deme sizes\n")
output_file.write(inideme_res)
output_file.write("\n")



output_file.close()

