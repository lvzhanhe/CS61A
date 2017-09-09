In this project, you will develop a simulator and multiple strategies for the dice game Hog. You will need to use *control statements* and *higher-order functions* together, as described in Sections 1.2 through 1.6 of [Composing Programs](http://composingprograms.com/).

In Hog, two players alternate turns trying to be the first to end a turn with at least 100 total points. On each turn, the current player chooses some number of dice to roll, up to 10. That player's score for the turn is the sum of the dice outcomes.

To spice up the game, we will play with some special rules:

- **Pig Out**. If any of the dice outcomes is a 1, the current player's score for the turn is 1.
  - *Example 1*: The current player rolls 7 dice, 5 of which are 1's. They score 1 point for the turn.
  - *Example 2*: The current player rolls 4 dice, all of which are 3's. Since Pig Out did not occur, they score 12 points for the turn.
- **Free Bacon**. A player who chooses to roll zero dice scores one more than the largest digit in the opponent's total score.
  - *Example 1*: If the opponent has 42 points, the current player gains 1 + max(4, 2) = 5 points by rolling zero dice.
  - *Example 2*: If the opponent has 48 points, the current player gains 1 + max(4, 8) = 9 points by rolling zero dice.
  - *Example 3*: If the opponent has 7 points, the current player gains 1 + max(0, 7) = 8 points by rolling zero dice.
- **Hogtimus Prime**. If a player's score for the turn is a prime number, then the turn score is increased to the next larger prime number. For example, if the dice outcomes sum to 11, given that none of the dice outcomes are 1, the current player scores 13 points for the turn. This boost only applies to the current player. *Note:* 1 is not a prime number!
- **Perfect Piggy**. If a player's score for the turn is not a 1, but is a perfect square or a perfect cube, the player scores the turn score but swaps the normal six-sided dice with four-sided dice for all subsequent turns. The next time either player activates Perfect Piggy, the six-sided dice will be swapped back. Subsequent activations of Perfect Piggy will continue swapping the dice.
- **Swine Swap**. After the turn score is added, if one of the scores is double the other, then the two scores are swapped.
  - *Example 1*: The current player has a total score of 37 and the opponent has 92. The current player rolls two dice that total 9. The current player's new total score (46) is half of the opponent's score. These scores are swapped! The current player now has 92 points and the opponent has 46. The turn ends.
  - *Example 2*: The current player has 91 and the opponent has 55. The current player rolls five dice that total 17, a prime that is boosted to 19 points for the turn (*Hogtimus Prime*). The current player has 110, so the scores are swapped. The opponent ends the turn with 110 and wins the game.