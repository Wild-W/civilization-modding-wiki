---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_FREE_BUILDING_WHEN_SPECIALTY_DISTRICT_CONSTRUCTED_EXCEPT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_FREE_BUILDING_WHEN_SPECIALTY_DISTRICT_CONSTRUCTED_EXCEPT
>
> * Class: `PLAYERS`
> * Parameters:
>	* DistrictType `Unknown`

## Samples
```SQL {title="TRAIT_FREE_BUILDING_WHEN_DISTRICT_MADE_EXCEPT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_FREE_BUILDING_WHEN_DISTRICT_MADE_EXCEPT",
		"MODIFIER_PLAYER_DISTRICT_ADJUST_FREE_BUILDING_WHEN_SPECIALTY_DISTRICT_CONSTRUCTED_EXCEPT"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_FREE_BUILDING_WHEN_DISTRICT_MADE_EXCEPT",
		"DistrictType",
		"DISTRICT_GOVERNMENT"
	);
	
```

