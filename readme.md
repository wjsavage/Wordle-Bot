# Wordle Bot
This programme is build to provide word suggestions for he popular online game: [Wordle](https://www.powerlanguage.co.uk/wordle/)

## How to play
When asked for feedback, enter the colour of each square from the game in a row
   
- 0 = grey
- 1 = yellow
- 2 = green
   
For example:
   - 01200 means the first, fourth and fifth letters were grey (not in word)
   - the second letter is yellow (in the word but a different location)
   - the third letter is green (in the word and in the correct position)

The system will then generate a suggested word. 

If Wordle refuses this word then enter 'n' when asked 'Was valid word? [y/n]', otherwise enter 'y'