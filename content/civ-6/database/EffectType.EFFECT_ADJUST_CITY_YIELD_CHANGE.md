---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_YIELD_CHANGE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_YIELD_CHANGE
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples
```SQL {title="MINOR_CIV_SCIENTIFIC_YIELD_FOR_CAPITAL"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"MINOR_CIV_SCIENTIFIC_YIELD_FOR_CAPITAL",
		"MODIFIER_PLAYER_CAPITAL_CITY_ADJUST_CITY_YIELD_CHANGE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"MINOR_CIV_SCIENTIFIC_YIELD_FOR_CAPITAL",
		"Amount",
		2
	),
	(
		"MINOR_CIV_SCIENTIFIC_YIELD_FOR_CAPITAL",
		"YieldType",
		"YIELD_SCIENCE"
	);
	
```

