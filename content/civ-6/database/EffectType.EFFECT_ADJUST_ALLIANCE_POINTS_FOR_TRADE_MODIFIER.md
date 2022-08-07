---
tags:
- EffectType
title: EFFECT_ADJUST_ALLIANCE_POINTS_FOR_TRADE_MODIFIER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_ALLIANCE_POINTS_FOR_TRADE_MODIFIER
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="TRAIT_ALLIANCE_POINTS_FROM_TRADE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_ALLIANCE_POINTS_FROM_TRADE",
		"MODIFIER_PLAYER_ADJUST_ALLIANCE_POINTS_FOR_TRADE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_ALLIANCE_POINTS_FROM_TRADE",
		"Amount",
		1
	);
	
```

