#Task-2

x = input('Enter text to write to the file: ')
file1 = open('output.txt','w')
writing_file = file1.write(x + '\n')
file1.close()
print('Data successfully written to output.txt.')
file1.close()


y = input('Enter additional text to append: ')
file1 = open('output.txt','a')
appending_file = file1.write(y + '\n')
file1.close()
print('Data successfully appended.')
file1.close()


print('Final contents of output.txt: ')
file1 = open('output.txt','r')
reading_file = file1.read()
print(reading_file)
file1.close()
