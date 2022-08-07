---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_DISTRICT_CREATE_UNIT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_DISTRICT_CREATE_UNIT
>
> * Class: `PLAYERS`
> * Parameters:
>	* DistrictType `String`
>		* [Districts.DistrictType]
>	* UnitType `String`
>		* [Units.UnitType]

## Samples

```SQL {title="TRAIT_FREE_APOSTLE_FINISH_MBANZA"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_FREE_APOSTLE_FINISH_MBANZA",
		"MODIFIER_PLAYER_DISTRICT_CREATE_UNIT"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_FREE_APOSTLE_FINISH_MBANZA",
		"DistrictType",
		"DISTRICT_MBANZA"
	),
	(
		"TRAIT_FREE_APOSTLE_FINISH_MBANZA",
		"UnitType",
		"UNIT_APOSTLE"
	);
	
```

