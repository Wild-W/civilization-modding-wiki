---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_SPY_COUNTERSPY_ENTIRE_CITY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_SPY_COUNTERSPY_ENTIRE_CITY
>
> * Class: `UNITS`
> * Parameters:
>	* EntireCity `Boolean`

## Samples
```SQL {title="SPY_SURVEILLANCE_ENTIRE_CITY"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"SPY_SURVEILLANCE_ENTIRE_CITY",
		"MODIFIER_SINGLE_UNIT_ADJUST_SPY_COUNTERSPY_ENTIRE_CITY"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"SPY_SURVEILLANCE_ENTIRE_CITY",
		"EntireCity",
		1
	);
	
```

