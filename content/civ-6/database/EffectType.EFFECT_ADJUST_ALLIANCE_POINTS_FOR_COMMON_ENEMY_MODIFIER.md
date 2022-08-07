---
tags:
- EffectType
title: EFFECT_ADJUST_ALLIANCE_POINTS_FOR_COMMON_ENEMY_MODIFIER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_ALLIANCE_POINTS_FOR_COMMON_ENEMY_MODIFIER
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="TRAIT_ALLIANCE_POINTS_FROM_COMMON_FOE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_ALLIANCE_POINTS_FROM_COMMON_FOE",
		"MODIFIER_PLAYER_ADJUST_ALLIANCE_POINTS_FOR_COMMON_FOE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_ALLIANCE_POINTS_FROM_COMMON_FOE",
		"Amount",
		2
	);
	
```

