---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_YIELD_PER_FLOOD
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_YIELD_PER_FLOOD
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples
```SQL {title="GREATBATH_FLOODFAITH"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"GREATBATH_FLOODFAITH",
		"MODIFIER_SINGLE_CITY_ADJUST_YIELD_FOR_FLOOD"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"GREATBATH_FLOODFAITH",
		"Amount",
		1
	),
	(
		"GREATBATH_FLOODFAITH",
		"YieldType",
		"YIELD_FAITH"
	);
	
```

