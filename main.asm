.gba
.thumb

.open "rom.gba", "test.gba", 0x08000000

// -----------------------------------------------------------------------------

.org allocation
.area allocation_size
    .importobj "build/linked.o"
.endarea

// -----------------------------------------------------------------------------

.org 0x08053B48
.area 0x15A, 0xFE
    ldr r3, =_CreateInGameTradePokemon |1
    bx r3
    .pool
.endarea

// skip over constants in the middle of the function

.org 0x08053CB4
.area 0x1A, 0xFE
.endarea

// -----------------------------------------------------------------------------

SIZEOF_INGAME_TRADE equ 0x3C

.if MOVE_INGAME_TRADE_ABILITYNUM

.org readu32("rom.gba", sInGameTradesPtr & 0x1FFFFFF)
.area NUM_INGAME_TRADES * SIZEOF_INGAME_TRADE
    .importobj "build/src/sInGameTrades.o"
.endarea

.endif

// -----------------------------------------------------------------------------

.close
