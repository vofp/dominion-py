import dominion as d
from cardnames import CardName as c
# game = d.initializeGame(2, [c.adventurer, c.ambassador, c.baron, c.council_room, c.cutpurse, c.embargo, c.feast, c.gardens, c.great_hall, c.mine], 10)
# print(d.whoseTurn(game))
# d.buyCard(c.silver, game)
# d.endTurn(game)
# print(d.whoseTurn(game))
# assert (d.buyCard(c.copper, game) == 0)
# print(d.whoseTurn(game))
# d.buyCard(c.silver, game)
# #assert (d.whoseTurn(game) == 1)
# assert (d.buyCard(c.silver, game) == -1)
# d.endTurn(game)
# assert (d.buyCard(c.province,game) == -1) 


def adventurer():
	game = d.initializeGame(2, [c.adventurer, c.ambassador, c.baron, c.council_room, c.cutpurse, c.embargo, c.feast, c.gardens, c.great_hall, c.mine], 10)

	game.currentPlayer().hand.append(c.adventurer)
	# print(game.currentPlayer().hand)

	# print(game.currentPlayer().deck)
	assert (d.playCard(5, -1, -1, -1, game) == 0)
	assert(game.currentPlayer().hand == [c.copper, c.estate, c.copper, c.copper, c.copper, c.copper, c.copper])
	assert(game.currentPlayer().deck == [c.copper, c.estate])
	return 0

adventurer()

def ambassador():
	game = d.initializeGame(2, [c.adventurer, c.ambassador, c.baron, c.council_room, c.cutpurse, c.embargo, c.feast, c.gardens, c.great_hall, c.mine], 10)

	game.currentPlayer().hand.append(c.ambassador)

	# print(game.currentPlayer().hand)
	assert (d.playCard(5, 0, 2, -1, game) == 0)
	assert(game.currentPlayer().hand == [c.estate, c.copper, c.copper, c.copper])
	assert(game.players[1].discard == [c.copper])

ambassador()

def baron():
	game = d.initializeGame(2, [c.adventurer, c.ambassador, c.baron, c.council_room, c.cutpurse, c.embargo, c.feast, c.gardens, c.great_hall, c.mine], 10)

	game.currentPlayer().hand.append(c.baron)
	# print(game.currentPlayer().coins)
	assert (d.playCard(5, 1, -1, -1, game) == 0)
	assert(game.currentPlayer().hand == [c.copper, c.copper, c.copper, c.copper])
	assert(game.currentPlayer().coins == 8)


	game = d.initializeGame(2, [c.adventurer, c.ambassador, c.baron, c.council_room, c.cutpurse, c.embargo, c.feast, c.gardens, c.great_hall, c.mine], 10)

	game.currentPlayer().hand.append(c.baron)
	# print(game.currentPlayer().coins)
	assert (d.playCard(5, 0, -1, -1, game) == 0)
	assert(game.currentPlayer().hand == [c.copper, c.estate, c.copper, c.copper, c.copper])
	assert(game.currentPlayer().discard == [c.baron, c.estate])
	assert(game.currentPlayer().coins == 4)

baron()

def council_room():
	game = d.initializeGame(2, [c.adventurer, c.ambassador, c.baron, c.council_room, c.cutpurse, c.embargo, c.feast, c.gardens, c.great_hall, c.mine], 10)

	game.currentPlayer().hand.append(c.council_room)
	p0 = d.numHandCards(game)
	p1 = len(game.players[1].hand)
	assert (d.playCard(5, -1, -1, -1, game) == 0)
	assert(p0 + 3 == d.numHandCards(game) )
	assert(p1+1 == len(game.players[1].hand))


council_room()









