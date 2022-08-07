---
tags:
- EffectType
title: EFFECT_ADJUST_EXTRA_ACCUMALATION_TERRAIN
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_EXTRA_ACCUMALATION_TERRAIN
>
> * Class: `Unknown`
> * Parameters:
>	* Amount `Integer`
>	* TerrainType `String`

## Samples

```SQL {title="TUNDRA_RESOURCE_EXTRACTION"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TUNDRA_RESOURCE_EXTRACTION",
		"MODIFIER_PLAYER_CITIES_ADJUST_EXTRA_ACCUMALATION_TERRAIN"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TUNDRA_RESOURCE_EXTRACTION",
		"Amount",
		100
	),
	(
		"TUNDRA_RESOURCE_EXTRACTION",
		"TerrainType",
		"TERRAIN_TUNDRA"
	);
	
```

