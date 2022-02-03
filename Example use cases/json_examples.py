import riceutils as utils # import the custom module
import os

# IF THIS IS BEING RUN FROM VSCODE
# make sure it is run from terminal

# cd "Example use cases"
# python json_examples.py

# it needs to be done in this way due to the way vscode uses directories

def main():
    currentDirectory = os.getcwd() # get the current working directory

    myJsonFile = utils.utils.open_read_json(f"{currentDirectory}\\testData.json") # open using custom function
    utils.utils.clear() # custom clear module
    print(f"\n\n\n{myJsonFile}")
    myJsonFile["name"] = input("Whats your name?\n>>>") # change the name attribute
    fileName = input("What would you like to call the file?\n>>>")
    result = utils.utils.write_save_json(f"{currentDirectory}\\{fileName}.json", myJsonFile) # save that to file

    if result == 1: # functions return 1 it was completed and nothing is expected back
        print("File save successful")
    elif result == -1: # and return -1 if they fail
        print("File save was unsuccessful")

if __name__ == "__main__":
    main()


# NOTE
# the write_save_json() function wont crash if the json file you are writing to does not exist
# instead it will create a new json file

