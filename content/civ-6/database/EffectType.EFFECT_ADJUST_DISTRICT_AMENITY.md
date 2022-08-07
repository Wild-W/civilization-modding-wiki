---
tags:
- EffectType
title: EFFECT_ADJUST_DISTRICT_AMENITY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_DISTRICT_AMENITY
>
> * Class: `DISTRICTS`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="WATER_WORKS_CANAL_AMENITY"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"WATER_WORKS_CANAL_AMENITY",
		"MODIFIER_CITY_DISTRICTS_ADJUST_DISTRICT_AMENITY",
		"DISTRICT_IS_CANAL"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"WATER_WORKS_CANAL_AMENITY",
		"Amount",
		1
	);
	
```

