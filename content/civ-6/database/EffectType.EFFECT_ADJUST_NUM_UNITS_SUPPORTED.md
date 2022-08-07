---
tags:
- EffectType
title: EFFECT_ADJUST_NUM_UNITS_SUPPORTED
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_NUM_UNITS_SUPPORTED
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`
>	* BuildingType `String`
>		* [Buildings.BuildingType]

## Samples

```SQL {title="TRAIT_SUPPORT_TWO_ARCHAEOLOGISTS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_SUPPORT_TWO_ARCHAEOLOGISTS",
		"MODIFIER_PLAYER_CITIES_ADJUST_NUM_UNITS_SUPPORTED"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_SUPPORT_TWO_ARCHAEOLOGISTS",
		"Amount",
		1
	),
	(
		"TRAIT_SUPPORT_TWO_ARCHAEOLOGISTS",
		"BuildingType",
		"BUILDING_MUSEUM_ARTIFACT"
	);
	
```

