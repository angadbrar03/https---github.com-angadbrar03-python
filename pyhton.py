def printBoard():

    print(f" 0 | 1 | 2")
    print(f"---|---|--")
    print(f" 3 | 4 | 5")
    print(f"---|---|--")
    print(f" 6 | 7 | 8")
    print(f"---|---|--")

if __name__ =="__main__":

    xState = [0, 0, 0, 0, 0, 0, 0, 0]
    zState = [0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1 # 1 for x and 0 for o
    print("welcome to kanta gole")
    while(true):
        if(turn == 1):
            print("x's chance")
            value = int (input("please enter a value"))
            xstate[value] = 1
        else:
            print("x's chance")
            value = input("please enter a value")
            zstate[value] = 1
    printBoard()
   break
