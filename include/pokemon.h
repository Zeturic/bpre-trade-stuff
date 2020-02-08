#pragma once

#include "constants/pokemon.h"

struct Pokemon
{
    /*0x00*/ u8 _[100];
};

struct BattleMove
{
    u8 effect;
    u8 power;
    u8 type;
    u8 accuracy;
    u8 pp;
    u8 secondaryEffectChance;
    u8 target;
    s8 priority;
    u8 flags;
};

extern struct Pokemon gPlayerParty[];
extern struct Pokemon gEnemyParty[];

void CalculateMonStats(struct Pokemon *mon);
u32 GetMonData(struct Pokemon *mon, s32 field);
void SetMonData(struct Pokemon *mon, s32 field, const void *dataArg);
void CreateMon(struct Pokemon *mon, u16 species, u8 level, u8 fixedIV, u8 hasFixedPersonality, u32 fixedPersonality, u8 otIdType, u32 fixedOtId);
u8 CalculatePPWithBonus(u16 move, u8 ppBonuses, u8 moveIndex);
