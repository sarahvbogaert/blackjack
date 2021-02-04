# blackjack
Simple Black Jack Game in Python command line user interface.

Black Jack (or Vingt-et-Un) is a comparing card game between one or more players and a dealer, where each player in turn competes against the dealer. Players do not compete against each other. The aim of the game is to reach a sum of cards closest to but below or equal to 21. It is played with one or more decks of 52 cards, and is the most widely played casino banking game in the world.

Players are each dealt two cards. The dealer is also dealt two cards. The value of cards two through ten is their pip value (2 through 10). Face cards (Jack, Queen, and King) are all worth ten. Aces can be worth one or eleven. A hand's value is the sum of the card values. Players are allowed to draw additional cards to improve their hands. A hand with an ace valued as 11 is called "soft", meaning that the hand will not burst by taking an additional card. The value of the ace will become one to prevent the hand from exceeding 21. Otherwise, the hand is called "hard".

Once all the players have completed their hands, it is the dealer's turn. The dealer hand will not be completed if all players have either busted or received blackjacks (see below). The dealer must hit (i.e. ask a new card) until the cards total up to 17 points. At 17 points or higher the dealer must stay (i.e. stop asking cards). (At most tables the dealer also hits on a "soft" 17, i.e. a hand containing an ace and one or more other cards totaling six.) You are betting that you have a better hand than the dealer. The better hand is the hand where the sum of the card values is closer to 21 without exceeding 21. The detailed outcome of the hand follows:

- If the player is dealt an Ace and a ten-value card (called a "blackjack" or "natural"), and the dealer does not, the player wins and usually receives a bonus.
- If the player exceeds a sum of 21 ("busts"), the player loses, even if the dealer also exceeds 21.
- If the dealer exceeds 21 ("busts") and the player does not, the player wins.
- If the player attains a final sum higher than the dealer and does not bust, the player wins.
- If both dealer and player receive a blackjack or any other hands with the same sum called a "push", no one wins.

If the player wins, he gets twice its bet. If no one wins, the player gets its bet back. If the player looses, he looses its bet.

To run the program, run the main script <b>black_jack.py</b>.
