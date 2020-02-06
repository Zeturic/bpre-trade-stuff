# where to start looking for free space
START_AT = 0x0871A240

# whether or not to move InGameTrade::abilityNum to make room for ::moveset
# 1 to opt in, 0 to opt out
# the standalone bpre-trade-movesets also makes this change,
# so if you have this already, make sure to set to 0
MOVE_INGAME_TRADE_ABILITYNUM = 1

# number of in-game trades in your ROM
# only used if MOVE_INGAME_TRADE_ABILITYNUM is 1,
# can be ignored otherwise
NUM_INGAME_TRADES = 9
