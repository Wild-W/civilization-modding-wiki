---
tags:
- EffectType
title: EFFECT_GRANT_UNIT_YIELD_ADJACENT_TERRAINS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_GRANT_UNIT_YIELD_ADJACENT_TERRAINS
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Integer`
>	* TerrainType `String`
>		* [Terrains.TerrainType]
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples
```SQL {title="GREATPERSON_ADJACENT_GRASSMOUNTAIN_SCIENCE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent
	)
VALUES
	(
		"GREATPERSON_ADJACENT_GRASSMOUNTAIN_SCIENCE",
		"MODIFIER_PLAYER_UNIT_GRANT_ADJACENT_TERRAIN_YIELD",
		1,
		1
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Type,
		Value
	)
VALUES
	(
		"GREATPERSON_ADJACENT_GRASSMOUNTAIN_SCIENCE",
		"Amount",
		"ScaleByGameSpeed",
		250
	),
	(
		"GREATPERSON_ADJACENT_GRASSMOUNTAIN_SCIENCE",
		"TerrainType",
		"ARGTYPE_IDENTITY",
		"TERRAIN_GRASS_MOUNTAIN"
	),
	(
		"GREATPERSON_ADJACENT_GRASSMOUNTAIN_SCIENCE",
		"YieldType",
		"ARGTYPE_IDENTITY",
		"YIELD_SCIENCE"
	);
	
```

