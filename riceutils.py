# refresh the power shell ONLY NEEDED IN SOME TESTING
# Get-Process -Id $PID | Select-Object -ExpandProperty Path | ForEach-Object { Invoke-Command { & "$_" } -NoNewScope }

# some basic utility functions
# pythab, pythac, root, soh, cah, toa
# get_clipboard, set_clipboard, clear, open_read_json, write_save_json
# vmath.vector3

# import any modules that are not standard
try:
    import clipboard as cl # clipboard is a module the must be installed seperatly
    clipboardModule = True
except:
    print("ERROR:\nNo clipboard module found. PIP install the clipboard module to use:\nget_clipboard()\nset_clipboard()\n\npip install clipboard")
    clipboardModule = False

# import standard python modules
from datetime import datetime
import math
import os
import json
import webbrowser





# FUNCTIONS 

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

def pythab(a,b): # pythagoras using sides a and b
    try:
        return math.sqrt(a**2 + b**2)
    except:
        return -1

def pythac(a,c): # pythagoras with the hypotenuse
    try:
        return math.sqrt(c**2 - a**2)
    except:
        return -1

def root(a,b): # a is the number b is the root
    try:
        return (a**(1/b))
    except:
        return -1

def clear(): # clear the console
    try:
        os.system("cls")
        return 1
    except:
        return -1

def soh(sine=0, oposite=0, hypotenuse=0): # input of sine must be in radians for the correct result to be outputed
    if sine == 0:
        return math.asin(oposite/hypotenuse)
    elif oposite == 0:
        return math.sin(sine)*hypotenuse
    elif hypotenuse == 0:
        return oposite/math.sin(sine)
    else:
        return -1

def cah(cosine=0, adjacent=0, hypotenuse=0): # input of sine must be in radians for the correct result to be outputed
    if cosine == 0:
        return math.acos(adjacent/hypotenuse)
    elif adjacent == 0:
        return math.cos(cosine)*hypotenuse
    elif hypotenuse == 0:
        return adjacent/math.cos(cosine)
    else:
        return -1

def toa(tangent=0, oposite=0, adjacent=0): # input of sine must be in radians for the correct result to be outputed
    if tangent == 0:
        return math.atan(oposite/adjacent)
    elif oposite == 0:
        return math.tan(tangent)*adjacent
    elif adjacent == 0:
        return oposite/math.tan(tangent)
    else:
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

def type_comparison(variable): # returns a string of a variables type. Use for printing the variable type neatly and easily? Type matching? Debugging?
    variable = str(type(variable))
    match variable: # not strictly supposed to be used for this. Im using it like this to avoid an if stack
        case "<class 'int'>":
            return "int"
        case "<class 'float'>":
            return "float"
        case "<class 'str'>":
            return "str"
        case "<class 'complex'>":
            return "complex"
        case "<class 'list'>":
            return "list"
        case "<class 'tuple'>":
            return "tuple"
        case "<class 'range'>":
            return "range"
        case "<class 'dict'>":
            return "dict"
        case "<class 'set'>":
            return "set"
        case "<class 'frozenset'>":
            return "frozenset"
        case "<class 'bool'>":
            return "bool"
        case "<class 'bytes'>":
            return "bytes"
        case "<class 'bytearray'>":
            return "bytearray"
        case "<class 'memoryview'>":
            return "memoryview"
        case _:
            print ("Possible custom data type? Not recognised")
            return -1

def open_browser(webName): # open up the default browser to a specified webpage
    try:
        webbrowser.open(f"https://www.{webName}")
    except:
        return -1

# result = utils.traverse_directories(os.getcwd(), allFiles=[], writeToFile=True, exceptions=[".git", "__pycache__",".tmp.drivedownload",".tmp.driveupload","build"]) run from Coding directory
def traverse_directories(path, allFiles, writeToFile=False, **exceptions): # traverse files from the starting directory of the python file
    startTime = datetime.now()

    exceptions = exceptions
    def container(path, allFiles):
        contents = os.listdir(path)
        for x in range(0,len(contents)):
            temp = f"{path}\\{contents[x]}"
            try:
                if os.path.isdir(temp):
                    if contents[x] not in exceptions["exceptions"]: # check for exceptions
                        container(temp, allFiles) # run function for new folder
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

# CLASSES

class vmath: # vmath class used as a sort of container for any expresions involving the vector3
    def __init__(self):
        pass

    def addition(self, *vectors): # adds an unspecified number of vector3's together
        X, Y, Z = 0, 0, 0
        for x in range(0, len(vectors)):
            X += vectors[x].out_x()
            Y += vectors[x].out_y()
            Z += vectors[x].out_z()
        return vmath.vector3(X, Y, Z)

    class vector3: # primative vector3 data format x,y,z

        def __init__(self, x=0,y=0,z=0):
            self.x = x
            self.y = y
            self.z = z

        # outputing functions
        def out(self):
            return self.x, self.y, self.z
        def out_x(self):
            return self.x
        def out_y(self):
            return self.y
        def out_z(self):
            return self.z

        # re-write variables
        def write(self,x,y,z):
            self.x = x
            self.y = y
            self.z = z
        def write_x(self,x):
            self.x = x
        def write_y(self,y):
            self.y = y
        def write_z(self,z):
            self.z = z

        # mathmatical functions
        def absolute(self):
            self.x = abs(self.x)
            self.y = abs(self.y)
            self.z = abs(self.z)

