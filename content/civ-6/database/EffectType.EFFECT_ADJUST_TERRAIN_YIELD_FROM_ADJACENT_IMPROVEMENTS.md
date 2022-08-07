---
tags:
- EffectType
title: EFFECT_ADJUST_TERRAIN_YIELD_FROM_ADJACENT_IMPROVEMENTS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_TERRAIN_YIELD_FROM_ADJACENT_IMPROVEMENTS
>
> * Class: `Unknown`
> * Parameters:
>	* Amount `Integer`
>	* ImprovementType `String`
>		* [Improvements.ImprovementType]
>	* TerrainType `String`
>		* [Terrains.TerrainType]
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples
```SQL {title="TRAIT_TERRACE_GRASS_MOUNTAIN"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_TERRACE_GRASS_MOUNTAIN",
		"MODIFIER_PLAYER_CITIES_ADJUST_TERRAIN_YIELD_FROM_ADJACENT_IMPROVEMENTS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_TERRACE_GRASS_MOUNTAIN",
		"Amount",
		1
	),
	(
		"TRAIT_TERRACE_GRASS_MOUNTAIN",
		"ImprovementType",
		"IMPROVEMENT_TERRACE_FARM"
	),
	(
		"TRAIT_TERRACE_GRASS_MOUNTAIN",
		"TerrainType",
		"TERRAIN_GRASS_MOUNTAIN"
	),
	(
		"TRAIT_TERRACE_GRASS_MOUNTAIN",
		"YieldType",
		"YIELD_FOOD"
	);
	
```

