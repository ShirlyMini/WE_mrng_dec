# open()

# writing data

# open('<path>/file1.txt', modes='w' or 'r' or 'a') #default mode is read

# fh = open('file1.log', 'w') # write# if the file exsist it will write the content
# # if the file exsist and it has content it will overwrite the content
# # if no file exsist the it will create and write
#
# fh.write("this is statement 11")
# fh.write("this is statement 12")
# fh.write("this is statement 13")
# fh.write("this is statement 14")
# fh.close()

# fh = open('file1.log', 'a') # write# if the file exsist it will write the content
# # if the file exsist and it has content it will append the content
# # if no file exsist the it will create and write
#
# fh.write("this is statement 21\n")
# fh.write("this is statement 22\n")
# fh.write("this is statement 23\n")
# fh.write("this is statement 24\n")
# fh.writelines(['this is statement 32', "this is statement 33", "this is statement 34"])
# fh.close()

# fh = open('file2.log')#FileNotFoundError
fh = open('file1.log')
# print(fh.read())
# print(fh.readlines())
print(fh.readline())
print(fh.readline())
print(fh.readline())
