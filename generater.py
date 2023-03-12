import random
import string
import os
import sys

# Set exeFileName as your exefile name ( e.g) wc209, ...)
exeFileName = 'test'

# Set Maximum Character number. (Less than 2 billion characters)
maxChar = 10000


os.system('rm outPut1/* && rm outPut2/* && rm randomTxtFiles/*')

'''  makeDirs(String path)
If input path directory not exist, make a directory
'''
def makeDirs(path):
  try:
    if not os.path.exists(path):
        os.makedirs(path)
  except OSError:
    print('Error !')

def compare(path1, path2):
  f1 = open(path1, 'r')
  f2 = open(path2, 'r')

  return f1.readline() != f2.readline()

# Get the number of file that want to generate.
numFiles = int(sys.argv[1])

# If user does not type the number of generate, print error message and exit.
if len(sys.argv) != 2:
  print("Error ! Please Type the number of files that want to generate !")
  sys.exit()

makeDirs('./randomTxtFiles')



txtFileName = "randomTxtFiles/random_text_"

prev_char = None
comment_bool = False

for fileNum in range(numFiles):
  f = open(txtFileName + str(fileNum) + '.txt', 'w')
  txtFileLength = random.randrange(1,maxChar)
  for i in range(txtFileLength) :
    rand_char = random.choice(string.printable)

    if rand_char == '*' and prev_char == '/' :
      comment_bool = True

    prev_char = rand_char
    f.write(rand_char)

  if comment_bool == True:
    f.write(' */')
    comment_bool = False


makeDirs('./outPut1')
makeDirs('./outPut2')

for fileNum in range(numFiles):
  print('Run ' + str(fileNum) +' files...')
  os.system('./' + exeFileName + ' < ' + txtFileName + str(fileNum) + '.txt > ' './outPut1/output1_' + str(fileNum))
  os.system('./' + 'samplewc209' + ' < ' + txtFileName + str(fileNum) + '.txt > ' './outPut2/output2_' + str(fileNum))

  if compare('./outPut1/output1_' + str(fileNum) , './outPut2/output2_' + str(fileNum)):
    print("Different At " + str(fileNum) + " File !")
    sys.exit()

