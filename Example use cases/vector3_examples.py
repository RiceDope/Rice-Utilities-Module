import riceutils as utils # import the custom module


def main():
    playersPosition = utils.vmath.vector3(5,5,5) # define the players position
    movement = utils.vmath.vector3(-7, 5, 4) # how much should the player be moving this update
    additionalMovement = utils.vmath.vector3(1,1,1) # some additional movement to show the addition method
    utils.clear() # custom clear module
    print(f"\n\n\nPlayers starting position: {playersPosition.out()}\nVector to translate the player by: {movement.out()}\nAdditional movement: {additionalMovement.out()}")

    result = utils.vmath() # create a vmath object to store the result
    playersPosition = result.addition(playersPosition, movement, additionalMovement) # output the result and update the players position

    print(f"Players ending position: {playersPosition.out()}")

if __name__ == "__main__":
    main()