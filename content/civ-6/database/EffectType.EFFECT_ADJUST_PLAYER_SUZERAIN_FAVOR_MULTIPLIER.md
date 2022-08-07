---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_SUZERAIN_FAVOR_MULTIPLIER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_SUZERAIN_FAVOR_MULTIPLIER
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="ORSZAGHAZ_DOUBLE_FAVOR_SUZERAIN"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"ORSZAGHAZ_DOUBLE_FAVOR_SUZERAIN",
		"MODIFIER_PLAYER_ADJUST_SUZERAIN_FAVOR_MULTIPLIER"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"ORSZAGHAZ_DOUBLE_FAVOR_SUZERAIN",
		"Amount",
		100
	);
	
```

