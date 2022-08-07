---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_YIELD_PER_TERRAIN_TYPE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_YIELD_PER_TERRAIN_TYPE
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`
>	* TerrainType `String`
>	* YieldType `String`

## Samples
```SQL {title="NAVIGATION_SCHOOL_NAVAL_COAST_SCIENCE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"NAVIGATION_SCHOOL_NAVAL_COAST_SCIENCE",
		"MODIFIER_CITY_ADJUST_CITY_YIELD_PER_TERRAIN_TYPE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"NAVIGATION_SCHOOL_NAVAL_COAST_SCIENCE",
		"Amount",
		"0.5"
	),
	(
		"NAVIGATION_SCHOOL_NAVAL_COAST_SCIENCE",
		"TerrainType",
		"TERRAIN_COAST"
	),
	(
		"NAVIGATION_SCHOOL_NAVAL_COAST_SCIENCE",
		"YieldType",
		"YIELD_SCIENCE"
	);
	
```

