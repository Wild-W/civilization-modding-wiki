---
tags:
- EffectType
title: EFFECT_ADJUST_IMPROVEMENT_VALID_TERRAIN
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_IMPROVEMENT_VALID_TERRAIN
>
> * Class: `Unknown`
> * Parameters:
>	* ImprovementType `String`
>	* TerrainType `String`

## Samples
```SQL {title="TUNDRA_FARMS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TUNDRA_FARMS",
		"MODIFIER_PLAYER_CITIES_ADJUST_IMPROVEMENT_VALID_TERRAIN"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TUNDRA_FARMS",
		"ImprovementType",
		"IMPROVEMENT_FARM"
	),
	(
		"TUNDRA_FARMS",
		"TerrainType",
		"TERRAIN_TUNDRA"
	);
	
```

