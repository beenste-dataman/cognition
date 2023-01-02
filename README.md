# cognition
A computing wormhole. My own personal framework for raw data analysis as a modular wormhole. 

---


Many applications! Open a directory and process all csv files. Choose a column and run an os command on every value in that column. Can change command and column between files. 



Always use '| tee file.txt' to save output. There is no output that works at this scale, sorry. Grep by filename to get it after. 



---



### This can run other scripts or tools, anything you'd run in cli is available. The target is static as the very last value in the command string. 

Structure is as such:

[command part1] + [command part 2] + [target]

Example to ping all values in a column:

You will input the following-
Command part 1: ping
Command part 2: -c 5

The Final command will be-
ping -c 5 target

With target being the value from the column in that iteration. 



---




#### Get nutso

- Run a script using this. 
- Build scripts to feed values from this. 
- Query API's 
- 
----

