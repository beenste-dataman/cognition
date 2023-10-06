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
...

print('-' * 55)
# get the directory path from the user
dir_path = input("Enter the directory path: ")

# loop through all the CSV files in the directory
for file in os.listdir(dir_path):
    if file.endswith(".csv"):
        print(art3)
        print('-' * 55)
        print('Starting this file: ' + file)
        print('-' * 55)

        # read the CSV file using pandas
        df = pd.read_csv(os.path.join(dir_path, file))
        ...
        
        # get the full command from the user
        print('-' * 55)
        full_command = input("Enter the full command with '{}' where the column value should be inserted: ")
        command_parts = full_command.split()
        print('-' * 55)
        
        print('Proceeding to run commands.')
        print('-' * 55)
        print('-' * 55)

        # loop through all the rows in the dataframe
        for index, row in df.iterrows():
            # get the value from the specified column
            target = str(row[col_name])
            # Replace the placeholder with the actual value
            full_command_for_value = [part.replace("{}", target) for part in command_parts]
            
            try:
                print(subprocess.run(full_command_for_value, text=True))
            except Exception as e:
                print(f"Error while running command on {target}. Error: {e}")

        print(art4)
        
print(art5)

