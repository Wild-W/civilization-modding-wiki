---
tags:
- EffectType
title: EFFECT_GRANT_BUILDING_IN_CITY_IGNORE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_GRANT_BUILDING_IN_CITY_IGNORE
>
> * Class: `CITIES`
> * Parameters:
>	* BuildingType `String`
>		* [Buildings.BuildingType]

## Samples
```SQL {title="GREATPERSON_WALLS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent
	)
VALUES
	(
		"GREATPERSON_WALLS",
		"MODIFIER_SINGLE_CITY_GRANT_BUILDING_IN_CITY_IGNORE",
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
		"GREATPERSON_WALLS",
		"BuildingType",
		"BUILDING_WALLS"
	);
	
```

