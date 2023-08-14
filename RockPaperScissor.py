series = int(input("Enter the number of matches: "))
p1=0
p2=0

for i in range(series):
    player1 = input("Player1 (R,P,S): ").upper()
    player2 = input("Player2 (R,P,S): ").upper()

    if player1==player2:
        print("Draw")
    elif (player1=='R' and player2=='S') or (player1=='S' and player2=='P') or (player1=='P' and player2=='R'):
        print("player1 wins")
        p1 += 1
    else:
        print("player2 wins")
        p2 += 1

if p1>p2:
    print("Player1 wins the series")
elif p1==p2:
    print("The series is Draw")
else:
    print("Player2 wins the series")