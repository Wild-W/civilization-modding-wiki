---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_ENTERTAINMENT_FROM_WONDER_ADJACENT_TO_LAKE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_ENTERTAINMENT_FROM_WONDER_ADJACENT_TO_LAKE
>
> * Class: `CITIES`
> * Parameters:
>	* BuildingType `String`
>		* [Buildings.BuildingType]

## Samples

```SQL {title="HUEY_ADDENTERTAINMENT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent
	)
VALUES
	(
		"HUEY_ADDENTERTAINMENT",
		"MODIFIER_SINGLE_CITY_ADJUST_LAKE_ENTERTAINMENT",
		1,
		1
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"HUEY_ADDENTERTAINMENT",
		"BuildingType",
		"BUILDING_HUEY_TEOCALLI"
	);
	
```

