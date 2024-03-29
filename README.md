## In-Game Trades

Adds a few more options for in-game trades.

Can also be used as sort of a trade editor to manage the new options.

For binary FR.

### Build Instructions

See [here](https://gist.github.com/Zeturic/db1611cc7b17c3140f9b9af32e1b596b) for the prequisites and help in installing them.

#### Cloning the repo

Open your terminal to whatever folder you want to download this repo into. Then, do the following to download the repo:

```shell
$ git clone https://github.com/Zeturic/bpre-trade-stuff.git
$ cd bpre-trade-stuff
```

#### Adding your ROM

Copy your ROM to this directory and rename it `rom.gba`.

#### Configuration

##### Compile Time Constants

Open `config.mk` in a text editor to set some compile-time configuration.

The build system is smart enough to find enough free space on its own, but if you want it to be inserted at a particular address, you can specify it by updating the definition of `START_AT`. If the given address is acceptable (i.e. is word-aligned and has enough bytes of free space), it will be inserted there. Otherwise, it will just use `START_AT` to determine where in the ROM it should start looking for free space.

Make sure to update `NUM_INGAME_TRADES` if you've repointed and expanded the table.

`InGameTrade::abilityNum` had to be moved in order to make room for `InGameTrade::moveset`. If the data in your ROM is already in this format, make sure to set `ABILITYNUM_HAS_ALREADY_BEEN_MOVED` to `1`, otherwise keep it as `0`.

If you've previously inserted this hack and just want to update the data without reinserting another copy of the code, you can set `INSERT_INGAME_TRADE_HACK` to `0`. Otherwise, keep it as `1`.

##### In-Game Trade Data

Run `make src/sInGameTrades.c` to extract the in-game trade data from your ROM. Then, you can open the newly created `src/sInGameTrades.c` in a text editor to modify `sInGameTrades` as desired.

Keep in mind that you can't add in-game trades by adding more elements to the end of `sInGameTrades`, because that would overwrite whatever happened to be after the table in your ROM. Instead, repoint `sInGameTrades` externally first, then use this with an updated `NUM_INGAME_TRADES`.

#### Building the project itself

Once you're ready, run `make`. This won't actually modify `rom.gba`, instead your output will be in `test.gba`. Naturally, test it in an emulator.

### On Trade Editors

The long and short of it is that this breaks trade editors. This is because it places new data in what used to be padding bytes, and trade editors could easily zero them out because they don't expect them to be meaningful or to need to be preserved.

Even worse, as mentioned above, `InGameTrade::abilityNum` had to be moved, and obviously trade editors will be looking for it at the old location, which is now part of `InGameTrade::moveset`, and obviously that would confuse them.

As a result, **do not use trade editors with this**.

Obviously, this lets you modify your trades when you're inserting this hack via `src/sInGameTrades.c`, but what if you want to modify them later on, long after you've added this?

This is why the options `INSERT_INGAME_TRADE_HACK` and `ABILITYNUM_HAS_ALREADY_BEEN_MOVED` exist in `config.mk`. They allow you to modify the data in your ROM by modifying `src/sInGameTrades.c` without reinserting the actual code, acting essentially as a text-based trade editor.

Alternatively, you can edit your trades using a hex editor.

### Notes

Most of the fields in the `InGameTrade` struct should be self-explanatory, but I'll explain the new ones anyway.

If `level` is set to `0`, the Pokémon's level will match the level of the Pokémon the player traded away. Otherwise, its level will be set to match the `level` field.

The `ivs` are listed in the following order: HP, Attack, Defense, Speed, Special Attack, Special Defense. If any of them are set to `0xFF`, that particular IV will be randomly generated. Otherwise, that IV will match the provided value.

An explanation of the `ppBonuses` byte can be found [here](https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_data_substructures_in_Generation_III#PP_bonuses).

An explanation of the `pokerus` byte can be found [here](https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9rus#Technical_information).

An explanation of the `ball` byte can be found [here](https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_data_substructures_in_Generation_III#Origins).

The `moveset` field is a pointer to moveset data. If it is set to `NULL`, the Pokémon will inherit the default moveset based on its level.

The moveset's format is dead simple; it's just four hwords corresponding to the move indices of the four chosen moves. Just make sure to put it at an address that is hword-aligned (ends in `0`, `2`, `4`, `6`, `8`, `A`, `C`, or `E`).

For example, if you wanted Reyley's Mimien to know Psychic (0x5E), Shadow Ball (0xF7), and Snatch (0x121), without a fourth move, you'd just do `5E 00 F7 00 21 01 00 00`. For the purposes of this example, we'll assume you inserted that at `0x08800900` with a hex editor.

Then, you can set the `moveset` field to `(u16*) 0x08800900` for Reyley's Mimien.

### Credits

The project structure and some of the build tools are from [pokeemerald](https://github.com/pret/pokeemerald).
