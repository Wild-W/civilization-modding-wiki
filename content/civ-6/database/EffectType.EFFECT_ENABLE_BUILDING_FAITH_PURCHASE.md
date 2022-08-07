---
tags:
- EffectType
title: EFFECT_ENABLE_BUILDING_FAITH_PURCHASE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ENABLE_BUILDING_FAITH_PURCHASE
>
> * Class: `CITIES`
> * Parameters:
>	* DistrictType `String`
>		* [Districts.DistrictType]

## Samples

```SQL {title="JESUIT_EDUCATION_SCIENCE_BUILDINGS_MODIFIER"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"JESUIT_EDUCATION_SCIENCE_BUILDINGS_MODIFIER",
		"MODIFIER_CITY_ENABLE_BUILDING_FAITH_PURCHASE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"JESUIT_EDUCATION_SCIENCE_BUILDINGS_MODIFIER",
		"DistrictType",
		"DISTRICT_CAMPUS"
	);
	
```

