max_strlen=[]
max_strindex=[]
for i in range(1,11):
    file_name="sample."+str(i)
    with open(file_name,"rb") as f:
        offsets=[]
        len_of_file=[]
        for strand in f.readlines():
            offsets.append(sum(len_of_file))
            len_of_file.append(len(strand))
        max_strlen.append(max(len_of_file))
        max_strindex.append(len_of_file.index(max(len_of_file)))
        print("The lengths of strand in file {} are:\n{}".format(file_name,str(len_of_file)[1:-1]))
        print("The offsets for each strand to appear in file {} are:\n{}".format(file_name,str(offsets)[1:-1]))
print("The file name of the largest strand that appears is: sample.{}".format(max_strlen.index(max(max_strlen))+1))
        
        
# file=open("sample.1","rb")
# # print(type(file.readlines()[1][:-1].decode("gbk")))
# # print(len(file.readline()[:-1]))
# # e=[]
# # for i in file.readlines():
# #     e.append(len(i))
# # print(sum(e))
# # print(file.read())
# print(len(file.read()))
