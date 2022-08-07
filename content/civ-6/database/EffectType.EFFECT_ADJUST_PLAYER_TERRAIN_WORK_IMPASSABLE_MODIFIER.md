---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_TERRAIN_WORK_IMPASSABLE_MODIFIER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_TERRAIN_WORK_IMPASSABLE_MODIFIER
>
> * Class: `PLAYERS`
> * Parameters:
>	* Ignore `Boolean`
>	* TerrainType `String`

## Samples

```SQL {title="TRAIT_WORK_GRASS_MOUNTAIN"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_WORK_GRASS_MOUNTAIN",
		"MODIFIER_PLAYER_ADJUST_TERRAIN_WORKABLE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_WORK_GRASS_MOUNTAIN",
		"Ignore",
		1
	),
	(
		"TRAIT_WORK_GRASS_MOUNTAIN",
		"TerrainType",
		"TERRAIN_GRASS_MOUNTAIN"
	);
	
```

