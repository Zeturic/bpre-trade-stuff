.gba
.thumb

.open "rom.gba", "test.gba", 0x08000000

.org allocation
.area allocation_size
    .importobj "build/linked.o"
.endarea

.org 0x08053B48
.area 0x15A, 0xFE
    ldr r3, =_CreateInGameTradePokemon |1
    bx r3
    .pool
.endarea

.org 0x08053CB4
.area 0x1A, 0xFE
.endarea

.close
