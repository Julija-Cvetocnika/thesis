import os
seq_dir = '/Users/julijacvetocnika/Lecture20Practical/test_dataset_fasta'
trim_out = '/Users/julijacvetocnika/Downloads/HIV_Study/test_dataset/trimmed_out'
standard1 =' SE -phred33 ' 
standard2 = ' ILLUMINACLIP:/Users/julijacvetocnika/Downloads/Trimmomatic-main/adapters/TruSeq3-SE.fa:2:30:10  LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36'


file_list = os.listdir(seq_dir)
print('# got list of files in: ' + seq_dir)

os.mkdir(trim_out)
print('# created subdir: ' + trim_out)

for seq in file_list:
   command_trim = 'trimmomatic' + standard1 + seq_dir + '/' + seq +' ' + trim_out + '/' + seq +'.trimmed' + standard2
   print(command_trim)
   os.system(command_trim)
