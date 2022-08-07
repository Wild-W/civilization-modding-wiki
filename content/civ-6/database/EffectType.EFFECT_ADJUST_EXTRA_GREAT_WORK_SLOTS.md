---
tags:
- EffectType
title: EFFECT_ADJUST_EXTRA_GREAT_WORK_SLOTS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_EXTRA_GREAT_WORK_SLOTS
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`
>	* BuildingType `String`
>		* [Buildings.BuildingType]
>	* GreatWorkSlotType `String`
>		* [GreatWorkSlotTypes.GreatWorkSlotType]

## Samples

```SQL {title="TRAIT_DOUBLE_ARCHAEOLOGY_SLOTS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_DOUBLE_ARCHAEOLOGY_SLOTS",
		"MODIFIER_PLAYER_CITIES_ADJUST_EXTRA_GREAT_WORK_SLOTS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_DOUBLE_ARCHAEOLOGY_SLOTS",
		"Amount",
		3
	),
	(
		"TRAIT_DOUBLE_ARCHAEOLOGY_SLOTS",
		"BuildingType",
		"BUILDING_MUSEUM_ARTIFACT"
	),
	(
		"TRAIT_DOUBLE_ARCHAEOLOGY_SLOTS",
		"GreatWorkSlotType",
		"GREATWORKSLOT_ARTIFACT"
	);
	
```

