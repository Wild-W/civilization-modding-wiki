---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_YIELD_PER_DISTRICT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_YIELD_PER_DISTRICT
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples
```SQL {title="MERITOCRACY_DISTRICTCULTURE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"MERITOCRACY_DISTRICTCULTURE",
		"MODIFIER_PLAYER_CITIES_ADJUST_CITY_YIELD_PER_DISTRICT"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"MERITOCRACY_DISTRICTCULTURE",
		"Amount",
		1
	),
	(
		"MERITOCRACY_DISTRICTCULTURE",
		"YieldType",
		"YIELD_CULTURE"
	);
	
```

