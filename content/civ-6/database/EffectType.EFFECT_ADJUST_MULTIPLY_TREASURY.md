---
tags:
- EffectType
title: EFFECT_ADJUST_MULTIPLY_TREASURY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_MULTIPLY_TREASURY
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="BIG_BEN_DOUBLE_GOLD"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent
	)
VALUES
	(
		"BIG_BEN_DOUBLE_GOLD",
		"MODIFIER_PLAYER_MULTIPLY_TREASURY",
		1,
		1
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"BIG_BEN_DOUBLE_GOLD",
		"Amount",
		100
	);
	
```

