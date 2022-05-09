# Operation UNO
## by Adnan Noorullah​, Alex Kwandou​, Matt Straczek, Jacob Stolker​
### adnann2, kwandou2, mstrac4, stolker2
---
Link for presentation used in video submission: https://uillinoisedu-my.sharepoint.com/:p:/g/personal/adnann2_illinois_edu/EUIPRkAbYCNJmROwqOoqURYBiZ2W_OPmtK0FoZwf7xEOAQ?e=W3Vloo
---
## Overview 
### Users can play UNO with
- Single Player mode ​
- AI with three difficulty modes​
- Player accounts
- Different rulesets/new cards​
- Real-life Sound effects​
- Theme music
- Custom graphics ​

---
## Why UNO?
- We wanted to create a recognizable game we all enjoy playing​
- We wanted to put our own spin on the game​
    - Custom rulesets, cards, mechanics are possible
- We were all interested in game development​
    - Adnan is also currently enrolled in CS 498 GD, which is the game dev course here at UIUC using UE4
- Wanted to develop a game which could potentially just be played for fun or as a stress-reliever (especially with finals coming up soon!)

### Roles
- Adnan Noorullah​ -> Graphics/Win Condition/UX
- Alex Kwandou​    -> Animations/Backend/Logic
- Matt Straczek   -> Graphics/Accounts/UX
- Jacob Stolker​   -> Mechanics/Logic/Testing

---

## How to Install
- The program requires python3 and the Pygame library to run.
- You can find directions to install Pygame at https://www.pygame.org/wiki/GettingStarted
- To pull our repository, clone into VS Code and cd into the repository using:
```
git clone https://github.com/CS222SP22/course-project-dh-a
cd course-project-dh-a
```
- To run the actual game, type: 
```python3 OperationUNO.py``` 
or 
```python OperationUNO.py``` 
in the terminal.

---

## Technical Architecture

- ### Libraries
    - Pygame     -> game functionality
    - numpy      -> data handling, game logic
    - unit-tests -> testing

- ### Components

    - Card    –> basic UNO card that contains color and value attributes​
    - Deck    –> contains multiple Card objects​
    - Player  –> represents a player of the game (both human and AI), contains information of their hand, handles placing a card​
    - AI      –> contains logic for different difficulties (governs the ai player's next move)​
    - Game    –> manages the Player objects, the Deck, and the current state of the game​
    - Ruleset –> tells Deck and Game how to initialize and run, and determines what is considered a valid move

- ### Menus
    - Main Menu          –> The home screen of the game​
    - Play Menu          –> Asks the user to choose between single player and multiplayer​
    - Settings Menu      –> Registration and login profiles​
    - Single player Menu –> User chooses how many bots and the difficulty​
    - Game Window        –> The game screen with all the animations and gameplay​
    - End Menu           –> Displays the winner and allows user to play again or quit game
 
 ![image](https://user-images.githubusercontent.com/82806112/166127080-0448a3a9-6747-40ee-8e61-fd999bcb1769.png)
