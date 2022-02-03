from datetime import datetime
import os
import json
import webbrowser

try:
    import clipboard as cl # clipboard is a module that must be installed seperatly
    clipboardModule = True
except:
    print("ERROR:\nNo clipboard module found. PIP install the clipboard module to use:\nget_clipboard()\nset_clipboard()\n\npip install clipboard")
    clipboardModule = False
    

def get_clipboard(): # returns the current clipboard
    if clipboardModule != False:
        return cl.paste()
    else:
        return -1

def set_clipboard(given): # copies given text to the clipboard
    if clipboardModule != False:
        cl.copy(given)
        return "done"
    else:
        return -1

def clear(): # clear the console
    try:
        os.system("cls")
        return 1
    except:
        return -1

def open_read_json(fileName): # takes in a full json file name and returns the contents
    try:
        with open(f"{fileName}", "r") as file:
            contents = file.read()
            contents = json.loads(contents)
        return(contents)
    except:
        return -1

def write_save_json(fileName, contents): # takes in a filename and a json string to write to a file. Replaces whole file
    try:
        contents = json.dumps(contents, indent=4, separators=(",",":"))
        with open(f"{fileName}", "w") as file:
            file.write(contents)
        return 1
    except:
        return -1

def open_browser(webName): # open up the default browser to a specified webpage
    try:
        webbrowser.open(f"https://www.{webName}")
    except:
        return -1

# could use update to check for file extentions
def traverse_directories(path, allFiles, writeToFile=False, exceptions=[""]): # traverse files from the starting directory of the python file
    startTime = datetime.now() # not best way of timing. But for quick implementation

    exceptions = exceptions
    def container(path, allFiles):
        contents = os.listdir(path)
        for x in range(0,len(contents)):
            temp = f"{path}\\{contents[x]}"
            try:
                if os.path.isdir(temp):
                    if contents[x] not in exceptions["exceptions"]: # check for exceptions
                        container(temp, allFiles) # run function for new folder. Ends up with a function stack
                else:
                    allFiles.append(contents[x]) # add the file to the list
            except:
                continue

        return allFiles
    
    result = container(path, allFiles)
    endTime = datetime.now()

    print(f"--COMPLETED THE TASK--\n\n\nDirectory exceptions: {exceptions}\nStart time: {startTime}\nEnd time: {endTime}")
    if writeToFile == True: # write to dump file in the directory of the search
        with open("dump.txt", "w") as file:
            file.write(str(result))
    return result # return search result to the user