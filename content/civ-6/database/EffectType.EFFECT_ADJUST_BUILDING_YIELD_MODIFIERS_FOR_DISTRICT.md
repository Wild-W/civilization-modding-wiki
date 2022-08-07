---
tags:
- EffectType
title: EFFECT_ADJUST_BUILDING_YIELD_MODIFIERS_FOR_DISTRICT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_BUILDING_YIELD_MODIFIERS_FOR_DISTRICT
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`
>	* DistrictType `String`
>		* [Districts.DistrictType]
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples

```SQL {title="FREEMARKET_BUILDING_YIELDS_HIGH_ADJACENCY"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"FREEMARKET_BUILDING_YIELDS_HIGH_ADJACENCY",
		"MODIFIER_PLAYER_CITIES_ADJUST_BUILDING_YIELD_MODIFIERS_FOR_DISTRICT",
		"COMMERCIAL_HUB_HAS_HIGH_ADJACENCY"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"FREEMARKET_BUILDING_YIELDS_HIGH_ADJACENCY",
		"Amount",
		50
	),
	(
		"FREEMARKET_BUILDING_YIELDS_HIGH_ADJACENCY",
		"DistrictType",
		"DISTRICT_COMMERCIAL_HUB"
	),
	(
		"FREEMARKET_BUILDING_YIELDS_HIGH_ADJACENCY",
		"YieldType",
		"YIELD_GOLD"
	);
	
```

