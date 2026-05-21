def main():
    """
    You should write your code here. 
    """
    milestontes = 20
    i=0
    player = ("Player 1")
    continueg = True

    while continueg:
        #If statement to know the player
        if i==0:
            player = ("Player 1")
            i = 1
        else:
            player = ("Player 2")
            i = 0

        print(f"There are {milestontes} stones left.")
        user_input = int(input(f"{player} would you like to remove 1 or 2 stones? "))
        
        while not (1 <= user_input <= 2):
            user_input = int(input("Please enter 1 or 2: "))
        milestontes = milestontes - user_input    
        
        if milestontes <=0:
            continueg = False
    #If statement to know the winner player
    if i==0:
        player = ("Player 1")
    else:
        player = ("Player 2")

    print(f"{player} wins!")    


if __name__ == '__main__':
    main()