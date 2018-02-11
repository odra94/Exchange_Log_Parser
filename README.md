# Exchange Log Parser
## By: Oscar Reyes

### Required: Python 3.6 

I created this program for work because we analyze different types of exchange logs. In our case we analyze IIS,  
OWA, EWS and EAS logs. All these logs have entries that are separated by commas and semicolons. This program  
focuses on this and parses each line in the log as an entry. Each entry is then split at each of these delimiters.  
These splits are then written to a new file in a more organized way. The output file corresponding to each input  
file makes each log entry easier to read and understand which in turn saves us time and effort.


**Running on Unix Based Systems:**  
1. Save "Parser.py" in the same directory where you have stored the logs you wish to parse.  
2. Open up your terminal and move into the directory where you stored "Parser.py."  
3. Once you are in that directory run the program by typing: python3.6 Parser.py  
4. The program will start and prompt you for the name of the log you want to parse. Type it in and press enter.
5. The program will then ask you for the name you want to give the output file of the log you chose previously. Type  
it in and press enter.
6. Once you enter the names of the input file and output file the program will process the information and produce the  
output file for easier reading and understanding.  


**Running on Windows Based Systems**  
Make sure that you installed Python 3.6 and that during the installation Python was added to your path.  

1. Save "Parser.py" in the same directory where you have stored the logs you wish to parse.  
2. Open up the folder where you stored "Parser.py"  
3. Double click the "Parser.py" file
4. The program will start and prompt you for the name of the log you want to parse. Type it in and press enter.
5. The program will then ask you for the name you want to give the output file of the log you chose previously. Type  
it in and press enter.
6. Once you enter the names of the input file and output file the program will process the information and produce the  
output file for easier reading and understanding.  





