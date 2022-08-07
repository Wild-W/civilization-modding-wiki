---
tags:
- EffectType
title: EFFECT_ADJUST_BUILDING_PURCHASE_COST
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_BUILDING_PURCHASE_COST
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`
>	* BuildingType `String`
>		* [Buildings.BuildingType]

## Samples
```SQL {title="MINOR_CIV_VALLETTA_PURCHASE_CHEAPER_WALLS_BONUS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"MINOR_CIV_VALLETTA_PURCHASE_CHEAPER_WALLS_BONUS",
		"MODIFIER_PLAYER_CITIES_ADJUST_BUILDING_PURCHASE_COST"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"MINOR_CIV_VALLETTA_PURCHASE_CHEAPER_WALLS_BONUS",
		"Amount",
		50
	),
	(
		"MINOR_CIV_VALLETTA_PURCHASE_CHEAPER_WALLS_BONUS",
		"BuildingType",
		"BUILDING_WALLS"
	);
	
```

