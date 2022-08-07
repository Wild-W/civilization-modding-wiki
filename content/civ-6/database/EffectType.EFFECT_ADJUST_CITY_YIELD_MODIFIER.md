---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_YIELD_MODIFIER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_YIELD_MODIFIER
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples
```SQL {title="BROADWAY_ADDCULTUREYIELD"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"BROADWAY_ADDCULTUREYIELD",
		"MODIFIER_SINGLE_CITY_ADJUST_CITY_YIELD_MODIFIER"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"BROADWAY_ADDCULTUREYIELD",
		"Amount",
		20
	),
	(
		"BROADWAY_ADDCULTUREYIELD",
		"YieldType",
		"YIELD_CULTURE"
	);
	
```

