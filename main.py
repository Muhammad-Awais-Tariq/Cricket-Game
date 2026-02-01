import random

def toss():

  # Simulates a coin toss and lets the user or computer choose batting or bowling based on the outcome.
    
    print("\n--- Toss Time! --\n")
    Options = ['heads', 'tails']
    computer_choice = random.choice(Options)
    user_choice = input("Call the toss! Enter 'heads' or 'tails': ").lower()

    while user_choice not in Options:
        print("Oops! That's not a valid choice. Please enter 'heads' or 'tails'.")
        user_choice = input("Call the toss again: ").lower()

    print(f"\nThe coin spins... and it's {computer_choice.upper()}!")
    if user_choice == computer_choice:
        print("🎉 You won the toss! 🎉")
        options = ['bat', 'bowl']
        user_option = input("What will you choose? 'bat' or 'bowl': ").lower()

        if user_option not in options:
            print("Invalid choice! Defaulting to 'bat'.")
            return 'bat'
    else:
        print("You lost the toss! The computer decides...")
        computer_option = random.choice(['bowl', 'bat'])
        print(f"The computer chooses to {computer_option}.")
        user_option = 'bowl' if computer_option == 'bat' else 'bat'

    return user_option

def play_innings(player_type, bowls, players):
    """
    Simulates an innings for either the user or the computer.
    """
    balls_played = 0
    score = 0
    wickets = 0
    numbers = [5, 4, 1, 2, 6, 3]

    print(f"\n--- {'Your' if player_type == 'user' else 'Computer\'s'} Innings Begin! ---")
    while wickets < players and balls_played < bowls:
        if player_type == "user":
            try:
                player_number = int(input("Enter your number (1-6): "))
                if player_number not in numbers:
                    print("⚠ Invalid number! Enter a number between 1 and 6.")
                    continue
            except ValueError:
                print("⚠ Invalid input! Please enter a number between 1 and 6.")
                continue
        else:
            player_number = random.choice(numbers)

        if player_type == "user":
            opponent_number = random.choice(numbers)
            print(f"Computer's number: {opponent_number}")
        else:
            try:
                opponent_number = int(input("Enter your number (1-6): "))
                print(f"Computer played: {player_number}")
                if opponent_number not in numbers:
                    print("⚠ Invalid number! Enter a number between 1 and 6.")
                    continue
            except ValueError:
                print("⚠ Invalid input! Please enter a number between 1 and 6.")
                continue

        if player_number != opponent_number:
            score += player_number
            print(f"🎯 Great shot! Your score is now: {score}")
        else:
            wickets += 1
            print("💔 Oh no! You lost a wicket. ")

        balls_played += 1
        print(f"The remaings bowls are : {bowls - balls_played}")

        if wickets == players:
            print(f"🏏 All players of {'you' if player_type == 'user' else 'computer'} are out!")
            break
        elif balls_played == bowls:
            print(f"⏳ Overs are over for {'you' if player_type == 'user' else 'computer'}.")

    print(f"🏆 Innings over! {'Your' if player_type == 'user' else 'Computer\'s'} final score: {score}\n")
    return score

def display_results(user_score, computer_score):
    """
    Displays the results of the match and declares the winner.
    """
    print("\n--- 🏆 Match Results 🏆 ---")
    print(f"Your Score: {user_score}")
    print(f"Computer's Score: {computer_score}")

    if user_score > computer_score:
        print("🎉 Congratulations! You won the match! 🎉")
    elif user_score < computer_score:
        print("😞 The computer won. Better luck next time!")
    else:
        print("🤝 It's a draw! What a match!")

def single_match(bowls , players):
    print("\n--- 🏏 Match Begins! ---")

    toss_result = toss()
    if toss_result is None:
        print("Invalid choice. Toss outcome switching to default bat.")
        toss_result = 'bat'

    if toss_result == "bat":
        user_score = play_innings("user", bowls, players)
        computer_score = play_innings("computer", bowls, players)
    else:
        computer_score = play_innings("computer", bowls, players)
        user_score = play_innings("user", bowls, players)

    display_results(user_score, computer_score)



def tournament(matches, bowls, players):
    """
    Simulates a tournament with multiple matches and calculates the overall winner.
    """
    user_tournament_score = 0
    computer_tournament_score = 0

    print("\n--- 🏏 Tournament Begins! ---")
    for match_number in range(1, matches + 1):
        print(f"\n--- Match {match_number} ---")

        toss_result = toss()
        if toss_result is None:
            print("Invalid choice. Toss outcome switching to default bat.")
            toss_result = 'bat'

        if toss_result == "bat":
            user_score = play_innings("user", bowls, players)
            computer_score = play_innings("computer", bowls, players)
        else:
            computer_score = play_innings("computer", bowls, players)
            user_score = play_innings("user", bowls, players)

        if user_score > computer_score:
            user_tournament_score += 1
        elif user_score < computer_score:
            computer_tournament_score += 1

        display_results(user_score, computer_score)

    print("\n--- 🏆 Tournament Results 🏆 ---")
    print(f"Your Wins: {user_tournament_score}")
    print(f"Computer's Wins: {computer_tournament_score}")

    if user_tournament_score > computer_tournament_score:
        print("🎉 You are the Tournament Champion! 🎉")
    elif user_tournament_score < computer_tournament_score:
        print("😞 The computer is the champion. Better luck next time!")
    else:
        print("🤝 The tournament ends in a draw! Incredible matches!")

def main():
    """
    Main function to start the cricket game.
    """
    print("🌟 Welcome to the Cricket World! 🌟")
    print("1️⃣ Play a match")
    print("2️⃣ Learn the rules")

    user_choice = input("Enter your choice (1 or 2): ").strip()
    
    if user_choice == "1":
        matches = int(input("Enter the number of matches: "))
        bowls = int(input("Enter the number of overs: ")) * 6
        players = int(input("Enter the number of players: "))

        if players > 11:
            print("⚠ You can't have more than 11 players. Exiting game.")
            return

        if matches > 1:
            print(f"🎮 Get ready for a tournament with {matches} matches!")
            tournament(matches, bowls, players)
        elif matches == 1:
            print("🎮 Starting a single match!")
            single_match(bowls , players )

    elif user_choice == "2":
        print("📜 Game Rules:")
        print("- Enter a number between 1 and 6 for each ball.")
        print("- If your number matches the opponent's number, you lose a wicket.")
        print("- The game ends when all players are out or overs are finished.")
        print("- Highest score wins the match!")

        choice = input("do you want to play a match :").lower()
        if choice =="yes":
            matches = int(input("Enter the number of matches: "))
            bowls = int(input("Enter the number of overs: ")) * 6
            players = int(input("Enter the number of players: "))

            if players > 11:
                print("⚠ You can't have more than 11 players. Exiting game.")
                return

            if matches > 1:
                print(f"🎮 Get ready for a tournament with {matches} matches!")
                tournament(matches, bowls, players)
            elif matches == 1:
                print("🎮 Starting a single match!")
                single_match(bowls , players )
        elif choice =="no":
            exit()
        else:
            print("⚠ Invalid input. Please restart the game.")

    
    else:
        print("⚠ Invalid input. Please restart the game.")

if __name__ == "__main__":
    main()
