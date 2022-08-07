---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_VALID_TERRAIN
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_VALID_TERRAIN
>
> * Class: `UNITS`
> * Parameters:
>	* TerrainType `String`
>		* [Terrains.TerrainType]
>	* Valid `Boolean`
>		* Whether or not the terrain type is valid to move into.

## Samples
```SQL {title="TRAIT_EARLY_OCEAN_NAVIGATION"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"TRAIT_EARLY_OCEAN_NAVIGATION",
		"MODIFIER_PLAYER_UNITS_ADJUST_VALID_TERRAIN",
		"PLAYER_HAS_SHIPBUILDING_TECH"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_EARLY_OCEAN_NAVIGATION",
		"TerrainType",
		"TERRAIN_OCEAN"
	),
	(
		"TRAIT_EARLY_OCEAN_NAVIGATION",
		"Valid",
		1
	);
	
```

