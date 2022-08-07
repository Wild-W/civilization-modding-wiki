---
tags:
- EffectType
title: EFFECT_IMPROVEMENT_ADJACENCY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_IMPROVEMENT_ADJACENCY
>
> * Class: `DISTRICTS`
> * Parameters:
>	* Amount `Integer`
>	* Description `String`
>	* DistrictType `String`
>		* [Districts.DistrictType]
>	* ImprovementType `String`
>		* [Improvements.ImprovementType]
>	* TilesRequired `Integer`
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples
```SQL {title="TRAIT_CIVILIZATION_GAUL_HOLYSITE_ADJACENCYFAITH"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_CIVILIZATION_GAUL_HOLYSITE_ADJACENCYFAITH",
		"MODIFIER_PLAYER_CITIES_IMPROVEMENT_ADJACENCY"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_CIVILIZATION_GAUL_HOLYSITE_ADJACENCYFAITH",
		"Amount",
		1
	),
	(
		"TRAIT_CIVILIZATION_GAUL_HOLYSITE_ADJACENCYFAITH",
		"Description",
		"LOC_DISTRICT_MINE_1_FAITH"
	),
	(
		"TRAIT_CIVILIZATION_GAUL_HOLYSITE_ADJACENCYFAITH",
		"DistrictType",
		"DISTRICT_HOLY_SITE"
	),
	(
		"TRAIT_CIVILIZATION_GAUL_HOLYSITE_ADJACENCYFAITH",
		"ImprovementType",
		"IMPROVEMENT_MINE"
	),
	(
		"TRAIT_CIVILIZATION_GAUL_HOLYSITE_ADJACENCYFAITH",
		"TilesRequired",
		2
	),
	(
		"TRAIT_CIVILIZATION_GAUL_HOLYSITE_ADJACENCYFAITH",
		"YieldType",
		"YIELD_FAITH"
	);
	
```

