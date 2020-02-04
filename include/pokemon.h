#pragma once

#include "constants/pokemon.h"

struct Pokemon
{
    /*0x00*/ u8 _[100];
};

extern struct Pokemon gPlayerParty[];
extern struct Pokemon gEnemyParty[];

void CalculateMonStats(struct Pokemon *mon);
u32 GetMonData(struct Pokemon *mon, s32 field);
void SetMonData(struct Pokemon *mon, s32 field, const void *dataArg);
void CreateMon(struct Pokemon *mon, u16 species, u8 level, u8 fixedIV, u8 hasFixedPersonality, u32 fixedPersonality, u8 otIdType, u32 fixedOtId);
