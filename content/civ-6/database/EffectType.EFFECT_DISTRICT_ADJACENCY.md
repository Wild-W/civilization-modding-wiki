---
tags:
- EffectType
title: EFFECT_DISTRICT_ADJACENCY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_DISTRICT_ADJACENCY
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`
>	* Description `String`
>	* DistrictType `String`
>		* [Districts.DistrictType]
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples
```SQL {title="TRAIT_ADJACENT_DISTRICTS_HOLYSITE_ADJACENCYFAITH"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_ADJACENT_DISTRICTS_HOLYSITE_ADJACENCYFAITH",
		"MODIFIER_PLAYER_CITIES_DISTRICT_ADJACENCY"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_ADJACENT_DISTRICTS_HOLYSITE_ADJACENCYFAITH",
		"Amount",
		1
	),
	(
		"TRAIT_ADJACENT_DISTRICTS_HOLYSITE_ADJACENCYFAITH",
		"Description",
		"LOC_DISTRICT_DISTRICT_1_FAITH"
	),
	(
		"TRAIT_ADJACENT_DISTRICTS_HOLYSITE_ADJACENCYFAITH",
		"DistrictType",
		"DISTRICT_HOLY_SITE"
	),
	(
		"TRAIT_ADJACENT_DISTRICTS_HOLYSITE_ADJACENCYFAITH",
		"YieldType",
		"YIELD_FAITH"
	);
	
```

