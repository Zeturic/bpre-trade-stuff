#!/usr/bin/env python3

import sys, os, io, struct, argparse
from pathlib import Path

import encoding

class InGameTrade():
    @staticmethod
    def parse(rom):
        trade = InGameTrade()

        trade.nickname = f'_("{encoding.decode(rom.read(11))}")'
        trade.pokerus, trade.species = struct.unpack("<BH", rom.read(3))
        trade.ivs = arraystring(rom.read(6))
        trade.abilityNum = struct.unpack("<B", rom.read(1))[0]
        rom.seek(3, os.SEEK_CUR)
        trade.otId = struct.unpack("<I", rom.read(4))[0]
        trade.conditions = arraystring(rom.read(5))
        rom.seek(3, os.SEEK_CUR)
        trade.personality, trade.heldItem, trade.mailNum = struct.unpack("<IHB", rom.read(7))
        trade.otName = f'_("{encoding.decode(rom.read(11))}")'
        trade.otGender, trade.sheen, trade.requestedSpecies, trade.level = struct.unpack("<BBHB", rom.read(5))
        trade.moveset = 0
        rom.seek(1, os.SEEK_CUR)

        return trade

    def __str__(self):
        return self.fmt.format(
            self.nickname,
            f"0x{self.pokerus :X}",
            f"0x{self.species :X}",
            self.ivs,
            self.abilityNum,
            self.otId,
            self.conditions,
            f"0x{self.personality :X}",
            f"0x{self.heldItem :X}",
            self.mailNum,
            self.otName,
            "FEMALE" if self.otGender else "MALE",
            self.sheen,
            f"0x{self.requestedSpecies :X}",
            self.level,
            f"(u16*) 0x{self.moveset :08X}" if self.moveset else "NULL"
        )

    with open(Path(__file__).parent / "templates/InGameTrade", "r", encoding="UTF-8") as stream:
        fmt = stream.read()

def arraystring(values):
    return "{" + ", ".join(str(value) for value in values) + "}"

def main():
    argparser = argparse.ArgumentParser(description='Rough automatic "decompilation" of sInGameTrades.')
    argparser.add_argument("--rom", required=True)
    argparser.add_argument("--pointer", dest="sInGameTradesPtr", required=True)
    argparser.add_argument("--num-trades", dest="NUM_INGAME_TRADES", required=True)
    argparser.add_argument("--output", required=True)

    args = argparser.parse_args()
    rom = args.rom
    output = args.output
    sInGameTradesPtr = int(args.sInGameTradesPtr, 0)
    NUM_INGAME_TRADES= int(args.NUM_INGAME_TRADES, 0)

    with open(rom, "rb") as stream:
        rom = io.BytesIO(stream.read())

    rom.seek(sInGameTradesPtr & 0x1FFFFFF)
    sInGameTrades = struct.unpack("<I", rom.read(4))[0]
    rom.seek(sInGameTrades & 0x1FFFFFF)

    trades = []

    for i in range(NUM_INGAME_TRADES):
        trades.append(InGameTrade.parse(rom))

    with open(Path(__file__).parent / "templates/sInGameTrades", "r", encoding="UTF-8") as stream:
        fmt = stream.read()

    with open(output, "w") as stream:
        stream.write(fmt.format("".join(str(trade) for trade in trades)))

if __name__ == "__main__":
    main()
