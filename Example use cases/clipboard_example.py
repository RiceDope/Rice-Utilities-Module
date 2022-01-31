import riceutils as utils # import the custom module

def main():

    utils.clear() # custom clear module

    yourName = input("\n\n\nWhat is your name>\n>>>")
    clipboardSave = utils.get_clipboard() # save the users current clipboard
    utils.set_clipboard(yourName) # put the users name to the clipboard

    utils.clear() # custom clear module
    print("\n\n\nYour name is copied to your clipboard")
    decision = input("We saved your clipboard from before would you like it back?(y/n)\n>>>") # take users decision

    if decision == "y":
        utils.clear() # custom clear module
        utils.set_clipboard(clipboardSave) # restore the users clipboard
        print("\n\n\nYour clipboard has been restored")


if __name__ == "__main__":
    main()