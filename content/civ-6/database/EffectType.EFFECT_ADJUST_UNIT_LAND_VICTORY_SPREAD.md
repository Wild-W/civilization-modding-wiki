---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_LAND_VICTORY_SPREAD
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_LAND_VICTORY_SPREAD
>
> * Class: `UNITS`
> * Parameters:
>	* LandVictorySpread `Boolean`

## Samples
```SQL {title="DISCIPLES_LAND_VICTORY_SPREAD"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"DISCIPLES_LAND_VICTORY_SPREAD",
		"MODIFIER_PLAYER_UNIT_ADJUST_LAND_VICTORY_SPREAD"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"DISCIPLES_LAND_VICTORY_SPREAD",
		"LandVictorySpread",
		1
	);
	
```

