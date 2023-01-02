import pandas as pd
import os
import subprocess


#ascii and stuff

art = '''
▄█▄    ████▄   ▄▀     ▄   ▄█    ▄▄▄▄▀ ▄█ ████▄    ▄   
█▀ ▀▄  █   █ ▄▀        █  ██ ▀▀▀ █    ██ █   █     █  
█   ▀  █   █ █ ▀▄  ██   █ ██     █    ██ █   █ ██   █ 
█▄  ▄▀ ▀████ █   █ █ █  █ ▐█    █     ▐█ ▀████ █ █  █ 
▀███▀         ███  █  █ █  ▐   ▀       ▐       █  █ █ 
                   █   ██                      █   ██ 
                                                      
'''


art2 = '''
|             |                                                                                                                                                                                                                 
|---.,   .    |---.,---.,---.,---.                                                                                                                                                                                              
|   ||   |    |   ||---'|---'|   |                                                                                                                                                                                              
`---'`---|    `---'`---'`---'`   '                                                                                                                                                                                              
     `---'                                                                                                                                                                                                                      
                                                                                                                                                                                                                                
                                                                                                                                                                                                                                
                                                                                                                                                                                                                                
                                                                                                                                                                                                                                
                                                                                                                                                                                                                                
                                                                                                                                                                                                                                
                                                                                                                                                                                                                                
,---.     o              |         |                                                               |        |    |    o|              ,---.                        |         |                             ,---.o|              
|  _.,---..,---.    . . .|---.,---.|--- ,---..    ,,---.,---.    ,   .,---..   .    . . .,---..   .|    ,---|    |    .|__/ ,---.     |__. ,---.,---.,-.-.    . . .|---.,---.|--- ,---..    ,,---.,---.    |__. .|--- ,---.     
|   |,---|||   |    | | ||   |,---||    |---' \  / |---'|        |   ||   ||   |    | | ||   ||   ||    |   |    |    ||  \ |---'     |    |    |   || | |    | | ||   |,---||    |---' \  / |---'|        |    ||    `---.     
`---'`---^``   '    `-'-'`   '`---^`---'`---'  `'  `---'`        `---|`---'`---'    `-'-'`---'`---'`---'`---'    `---'``   ``---'o    `    `    `---'` ' '    `-'-'`   '`---^`---'`---'  `'  `---'`        `    ``---'`---'o    
                                                                 `---'                                                                                                                                                          
'''


art3 = '''
=================================================================
=  =======  =========================        ======  ============
=   ======  =========================  ============  ============
=    =====  =========================  ============  ============
=  ==  ===  ===   ===  =   =  =======  ========  ==  ===   ======
=  ===  ==  ==  =  ==  =   =  =======      ========  ==  =  =====
=  ====  =  ==     ===   =   ========  ========  ==  ==     =====
=  =====    ==  ======   =   ========  ========  ==  ==  ========
=  ======   ==  =  ==== === =========  ========  ==  ==  =  ==  =
=  =======  ===   ===== === =========  ========  ==  ===   ===  =
=================================================================
'''

art4 = '''
=======================================================================================================
=       =============================  ====  ====  ============  ==========        ======  ============
=  ====  ============================  ====  ====  ============  ==========  ============  ============
=  ====  ============================  ====  ====  =======  ===  ==========  ============  ============
=  ====  ===   ===  = ====   ========  ====  ====  ==  ==    ==  ==========  ========  ==  ===   ======
=  ====  ==     ==     ==  =  =======   ==    ==  ========  ===    ========      ========  ==  =  =====
=  ====  ==  =  ==  =  ==     ========  ==    ==  ===  ===  ===  =  =======  ========  ==  ==     =====
=  ====  ==  =  ==  =  ==  ===========  ==    ==  ===  ===  ===  =  =======  ========  ==  ==  ========
=  ====  ==  =  ==  =  ==  =  =========    ==    ====  ===  ===  =  =======  ========  ==  ==  =  ==  =
=       ====   ===  =  ===   ===========  ====  =====  ===   ==  =  =======  ========  ==  ===   ===  =
=======================================================================================================
'''

art5 = '''
                                                                        
     .oo 8 8   ooo.                             .oPYo.                  
    .P 8 8 8   8  `8.                           8   `8                  
   .P  8 8 8   8   `8 .oPYo. odYo. .oPYo.      o8YooP' o    o .oPYo.    
  oPooo8 8 8   8    8 8    8 8' `8 8oooo8       8   `b 8    8 8oooo8    
 .P    8 8 8   8   .P 8    8 8   8 8.           8    8 8    8 8.        
.P     8 8 8   8ooo'  `YooP' 8   8 `Yooo' 88    8oooP' `YooP8 `Yooo' 88 
..:::::......::.....:::.....:..::..:.....:..::::......::....8 :.....:..:
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::ooP'.::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::...::::::::::::
'''





print('-' * 55)
print('-' * 55)
print(art)
print('-' * 55)

print(art2)
print('-' * 55)
print('-' * 55)
print('-' * 55)
print('Enter a directory. It will gather all files ending with csv. One by one you can choose a column.\n Then you choose a command to run on each value in that column.\n And so on... until the directory is out of csv files.\n You can change the command and column on each file. \n Use | tee to capture your output. For now. \n Bye.')
print('-' * 55)
print('When you enter your commands you will do it in two parts.\n The first part should be the name, include sudo and the name if sudo is needed (run as SU duh).\n  Then in the second part include all args.\n The final part will be the column value, it is the last value. Arrange accordingly.\n If you are some type of genius plz fix and send my way so we can mix and match.\n')
print('-' * 55)
# get the directory path from the user
dir_path = input("Enter the directory path: ")


#col_name = input("Enter the column name: ")



# loop through all the CSV files in the directory
for file in os.listdir(dir_path):
  if file.endswith(".csv"):
    print(art3)
    print('-' * 55)
    print('Starting this file: ' + file)
    print('-' * 55)

    # read the CSV file using pandas
    df = pd.read_csv(os.path.join(dir_path, file))
    print('-' * 55)
    print('-' * 55)
    print('Displaying first five rows of the csv file currently being processed: ')
    print('-' * 55)
    print(df.head())
    print('-' * 55)
    print('All column names: ')
    print(str(df.columns))
    print('-' * 55)
    print('Datatypes of all cols: ')
    print(df.dtypes)
    print('-' * 55)
    print('Summary stats if you need them: ')
    print(df.describe())
    print('-' * 55)
    print('The shape of this file is: ')
    print('-' * 55)
    print(df.shape)
    print('-' * 55)
    print('-' * 55)
    pause = input('Hit enter when ready to proceed to entering commands.')



    
    # get the column name from the user
    print('-' * 55)
    col_name = input('Now enter the column name for the command you would like run on the values in that column: ')
    print('-' * 55)
    # get the command from the user
    print('-' * 55)
    command = input('Now enter the first part of the command that you want to run on this column:s values: ')
    print('-' * 55)
    # get second part of command
    print('-' * 55)
    in1 = input('second part of command:')
    print('-' * 55)
    #433pm change
    
    #now add output results file for this file's iteration, w/ prompt and new file for each file iteration
    #results_file = input('Now enter name of a .txt file to save the results of this file`s specific iteration.\n You will do this for each file: ')
    #results_file = str(results_file)

    print('Proceeding to run commands.')
    print('-' * 55)
    print('-' * 55)


    # loop through all the rows in the dataframe
    for index, row in df.iterrows():
      # get the value from the specified column
      target = row[col_name]
      target = str(target)
      command = str(command)
      in1 = str(in1)
      #print(file)
      print('Value being run: ' + target)
      print(command + ' being run now. Results below: ')
      
      # run the command on the value
      try:
        print(subprocess.run([command, in1, target], text=True))
      except:
        pass
      #result = os.system(command.format(target))
      #print(result)
      # print the output
      #print(output)

    print(art4)
#say bye

print(art5)
