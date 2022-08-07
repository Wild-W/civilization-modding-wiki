---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_SPY_ESTABLISH_TIME
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_SPY_ESTABLISH_TIME
>
> * Class: `UNITS`
> * Parameters:
>	* ReductionPercent `Integer`

## Samples
```SQL {title="SPY_DISGUISE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"SPY_DISGUISE",
		"MODIFIER_PLAYER_UNIT_ADJUST_SPY_ESTABLISH_TIME"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"SPY_DISGUISE",
		"ReductionPercent",
		100
	);
	
```

