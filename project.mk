SRC_FILES = $(filter-out src/sInGameTrades.c, $(wildcard src/*.c))

EXTRA_CFLAGS = -D NUM_INGAME_TRADES=$(NUM_INGAME_TRADES) -D INSERT_INGAME_TRADE_HACK=$(INSERT_INGAME_TRADE_HACK)

EXTRA_LDFLAGS = --defsym sInGameTradesPtr=$(sInGameTradesPtr)

EXTRA_ARMIPS_FLAGS = -equ NUM_INGAME_TRADES $(NUM_INGAME_TRADES) -equ INSERT_INGAME_TRADE_HACK $(INSERT_INGAME_TRADE_HACK)

TRADESCANTIA = $(PYTHON) tools/tradescantia
TRADESCANTIA_FLAGS = --rom rom.gba --pointer $(sInGameTradesPtr) --num-trades $(NUM_INGAME_TRADES)

ifneq ($(ABILITYNUM_HAS_ALREADY_BEEN_MOVED),0)
TRADESCANTIA_FLAGS += --modified-format
endif

sInGameTradesPtr = 0x08053CA4

# ------------------------------------------------------------------------------

src/sInGameTrades.c: rom.gba
	$(TRADESCANTIA) $(TRADESCANTIA_FLAGS) --output "$@"

test.gba: build/src/sInGameTrades.o
