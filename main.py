import random
import time

from threading import Thread
from player import Player
from deck import Deck

me = Player()

opponent = Player()

players = [me, opponent]

deck = Deck()

print("How many decks would you like to play with?")

numberOfDecks = int(input())

cards = []

for x in range(numberOfDecks):
	deck = Deck()
	cards = cards + deck.cards

random.shuffle(cards)

playedCards = []

stopThread = False

def listenForSnap():
	global playedCards
	global stopThread

	while not stopThread:
		value = raw_input()

		if len(playedCards) >= 2 and playedCards[-1].value == playedCards[-2].value:
			print("SNAP!")
			me.cards = me.cards + playedCards
			playedCards = []

thread = Thread(target = listenForSnap)
thread.start()

while len(cards) > 0:
	card = cards.pop(0)
	playedCards.append(card)
	print(str(card.value) + " of " + card.suit)
	time.sleep(0.75)

if len(me.cards) > len(opponent.cards):
	print("YOU WIN!")
elif len(me.cards) == len(opponent.cards):
	print("YOU DRAW!")
else:
	print("YOU LOSE!")

stopThread = True
