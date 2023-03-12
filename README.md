# **This python file for Random Txt File Tester for EE209 Assignment 1**

### **User Guide**

1. Change the value of **'exeFileName'** to your exefile name in  **generater.py (line 7)**

   (exeFileName = 'YourExeFileName')
2. Change the value of 'maxChar' to maximum character number you want.

   (maxChar = MaximumCharacterNumberYouWant)
3. Type follow in directories that generator.py is exist.

   **`python3 generator.py NumberOfYouWantTest`**

   ex)

   `python3 generator.py 100`

   This will be test for 100 random txt files.

---

#### This python file makes a directories **randomTxtFiles, outPut1, outPut2**

* randomTxtFiles : The random txt files
  * In randomTxtFiles, there are txt files that generated named random_text_numberOfTested (e.g random_text_3)
* outPut1 : The output of your code
  * In outPut1, there are output files named output1_numberOfTested (e.g output1_3).
* outPut2 : The output of samplewc209
  * In outPut2, there are output files named output2_numberOfTested (e.g output2_3).

#### If your codes output is different from samplewc209, python code will stop the test and tell you what random txt file makes your code wrong.

For example, if your code different from samplewc209 at third random txt file, then python will stop the test and tell like below.

`Different At 3 File !`

Then, you can check that number 3 random txt file at

*randomTxtFiles/random_text_3.txt*
