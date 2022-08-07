---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_YIELD_PER_TERRAIN_CLASS_CITIES_IMPROVEMENT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_YIELD_PER_TERRAIN_CLASS_CITIES_IMPROVEMENT
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`
>	* ImprovementType `String`
>	* YieldType `String`

## Samples

```SQL {title="OPEN_AIR_MUSEUM_CULTURE_FOR_TERRAIN_CLASS_CITIES"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"OPEN_AIR_MUSEUM_CULTURE_FOR_TERRAIN_CLASS_CITIES",
		"MODIFIER_SINGLE_CITY_ADJUST_YIELD_FOR_TERRAIN_CLASS_CITIES_IMPROVEMENT"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"OPEN_AIR_MUSEUM_CULTURE_FOR_TERRAIN_CLASS_CITIES",
		"Amount",
		2
	),
	(
		"OPEN_AIR_MUSEUM_CULTURE_FOR_TERRAIN_CLASS_CITIES",
		"ImprovementType",
		"IMPROVEMENT_OPEN_AIR_MUSEUM"
	),
	(
		"OPEN_AIR_MUSEUM_CULTURE_FOR_TERRAIN_CLASS_CITIES",
		"YieldType",
		"YIELD_CULTURE"
	);
	
```

