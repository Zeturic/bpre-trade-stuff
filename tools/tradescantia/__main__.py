#!/usr/bin/env python3

import sys, os, io, struct, argparse
from pathlib import Path

import encoding

class InGameTrade():
    @staticmethod
    def parse(rom, *, original_format):
        trade = InGameTrade()

        (
            trade.nickname,
            trade.pokerus,
            trade.species,
            trade.ivs,
            maybe_moveset,
            trade.otId,
            trade.conditions,
            trade.ppBonuses,
            trade.ball,
            _,
            trade.personality,
            trade.heldItem,
            trade.mailNum,
            trade.otName,
            trade.otGender,
            trade.sheen,
            trade.requestedSpecies,
            trade.level,
            maybe_abilityNum,
        ) = struct.unpack("11sBH6sII5sBBBIHB11sBBHBB", rom.read(60))

        if original_format:
            trade.abilityNum = maybe_moveset & 0xFF
            trade.moveset = 0
        else:
            trade.abilityNum = maybe_abilityNum
            trade.moveset = maybe_moveset

        trade.nickname = encoding.decode(trade.nickname)
        trade.otName = encoding.decode(trade.otName)

        trade.ivs = list(trade.ivs)
        trade.conditions = list(trade.conditions)

        return trade

    def __str__(self):
        return self.fmt.format(
            f'_("{self.nickname}")',
            f"0x{self.pokerus :X}",
            f"0x{self.species :X}",
            arraystring(self.ivs),
            self.abilityNum,
            self.otId,
            arraystring(self.conditions),
            f"0x{self.personality :X}",
            f"0x{self.heldItem :X}",
            self.mailNum,
            f'_("{self.otName}")',
            "FEMALE" if self.otGender else "MALE",
            self.sheen,
            f"0x{self.requestedSpecies :X}",
            self.level,
            f"(u16*) 0x{self.moveset :08X}" if self.moveset else "NULL",
            f"0x{self.ppBonuses :X}",
            self.ball
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
    argparser.add_argument("--modified-format", dest="original_format", action="store_false")
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
        trades.append(InGameTrade.parse(rom, original_format=args.original_format))

    with open(Path(__file__).parent / "templates/sInGameTrades", "r", encoding="UTF-8") as stream:
        fmt = stream.read()

    with open(output, "w") as stream:
        stream.write(fmt.format("".join(str(trade) for trade in trades)))

if __name__ == "__main__":
    main()
