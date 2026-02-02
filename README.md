# Cricket-Game
Its a simple console-based Python game that includes a toss system. The user plays against the computer. It supports single matches as well as tournaments consisting of multiple matches, and it follows easy-to-understand cricket-inspired rules.

## Features
- Coin toss (*Heads / Tails*)
- Choice to bat or bowl after toss
- Play
  - *Single match*
  - *Tournament*
- Any number of players up to **11**
- Custom overs (*no upper limit*)
- Computer opponent with random choices
- Automatic winner declaration

## How the Game Works
This game is inspired by *hand cricket*, where both players choose a number between **1 and 6**
### Toss Rules
- You can select *Heads* or *Tails*
- If the toss is won, then you can select:
  - **Bat**
  - **Bowl**
- If lost, the computer automatically decides

### Batting & Bowling Rules
- On each bowl:
  - Both players choose a number between **1 and 6**
- If the numbers are different:
  - Then the batting player scores runs equal to their number
- If the numbers are the same:
  - Then the batting player loses a wicket

## **End of an Innings**
An innings ends when:
- All players are out
or
- All overs are completed

## **Match Result**
- Player with the higher score wins
- If the score is equal, then it is a *draw*

## **Tournament Rules**
- Each tournament consists of multiple matches
- Each match winner gets **one point**
- The player with the most points wins the tournament

## **How to Run the Game**
1. Make sure **Python** is installed
2. Save the file as `cricket_game.py`
3. Run the program
```bash
python cricket_game.py
```

## Menu Options
when the game starts:
1. Play the Match
2. Learn the rules
Follow on screen instructions to play.

## File Structure
```bash
project/
│── file.py
│── README.md
```

## Technologies Used
- Python
- Build in random module

## Notes
- Maximum 11 players are allowed
- invalid inputs are handled savely
- Designed for learning and fun

## Author
Muhammad Awais Tariq

---
If you like this project, consider giving it a star on GitHub!
