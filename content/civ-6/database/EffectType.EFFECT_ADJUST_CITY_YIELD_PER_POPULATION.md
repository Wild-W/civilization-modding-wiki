---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_YIELD_PER_POPULATION
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_YIELD_PER_POPULATION
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples
```SQL {title="PRASAT_CULTURE_POPULATION"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"PRASAT_CULTURE_POPULATION",
		"MODIFIER_SINGLE_CITY_ADJUST_CITY_YIELD_PER_POPULATION"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"PRASAT_CULTURE_POPULATION",
		"Amount",
		"0.5"
	),
	(
		"PRASAT_CULTURE_POPULATION",
		"YieldType",
		"YIELD_CULTURE"
	);
	
```

