---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_COUNTER_SPY_YIELD_AWARD_PER_LEVEL
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_COUNTER_SPY_YIELD_AWARD_PER_LEVEL
>
> * Class: `Unknown`
> * Parameters:
>	* Amount `Unknown`
>	* PerXLevels `Unknown`
>	* YieldType `Unknown`

## Samples

```SQL {title="CHANCERY_COUNTERYSPY_SCIENCE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"CHANCERY_COUNTERYSPY_SCIENCE",
		"MODIFIER_PLAYER_ADJUST_COUNTER_SPY_AWARD_YIELD_PER_LEVEL"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"CHANCERY_COUNTERYSPY_SCIENCE",
		"Amount",
		50
	),
	(
		"CHANCERY_COUNTERYSPY_SCIENCE",
		"PerXLevels",
		1
	),
	(
		"CHANCERY_COUNTERYSPY_SCIENCE",
		"YieldType",
		"YIELD_SCIENCE"
	);
	
```

