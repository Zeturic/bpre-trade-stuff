# where to start looking for free space
START_AT = 0x0871A240

# number of in-game trades in your ROM
NUM_INGAME_TRADES = 9

# InGameTrade::abilityNum had to be moved to make room for ::moveset
# the standalone bpre-trade-movesets also makes this change,
# 	if your ROM already has this change, set to 1
# 1 for yes, 0 for no
ABILITYNUM_HAS_ALREADY_BEEN_MOVED = 0

# if your ROM already has the code and you just want to update data,
#	you can avoid re-inserting the code
# 1 for yes, 0 for no
INSERT_INGAME_TRADE_HACK = 1
