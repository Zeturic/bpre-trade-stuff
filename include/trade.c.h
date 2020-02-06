#pragma once

#include "trade.h"

struct InGameTrade {
    /*0x00*/ u8 nickname[POKEMON_NAME_LENGTH + 1];
    /*0x0B*/ u8 pokerus;
    /*0x0C*/ u16 species;
    /*0x0E*/ u8 ivs[NUM_STATS];
    /*0x14*/ u16 *moveset;
    /*0x18*/ u32 otId;
    /*0x1C*/ u8 conditions[CONTEST_CATEGORIES_COUNT];
    /*0x21*/ u8 pad_21;
    /*0x22*/ u8 pad_22;
    /*0x23*/ u8 pad_23;
    /*0x24*/ u32 personality;
    /*0x28*/ u16 heldItem;
    /*0x2A*/ u8 mailNum;
    /*0x2B*/ u8 otName[11];
    /*0x36*/ u8 otGender;
    /*0x37*/ u8 sheen;
    /*0x38*/ u16 requestedSpecies;
    /*0x3A*/ u8 level;
    /*0x3B*/ u8 abilityNum;
};

#ifndef SKIP_DECLARE_SINGAMETRADES

// extern const struct InGameTrade sInGameTrades[];
typedef const struct InGameTrade sInGameTradesType[];
extern const sInGameTradesType * const sInGameTradesPtr;
#define sInGameTrades (*sInGameTradesPtr)

#endif

void SetInGameTradeMail(struct MailStruct *mail, const struct InGameTrade *trade);
