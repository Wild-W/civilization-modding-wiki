---
tags:
- EffectType
title: EFFECT_ADJUST_PLOT_PURCHASE_COST_TERRAIN
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLOT_PURCHASE_COST_TERRAIN
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`
>	* TerrainType `String`

## Samples

```SQL {title="TUNDRA_PLOT_COST"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TUNDRA_PLOT_COST",
		"MODIFIER_PLAYER_CITIES_ADJUST_PLOT_PURCHASE_COST_TERRAIN"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TUNDRA_PLOT_COST",
		"Amount",
		"-50"
	),
	(
		"TUNDRA_PLOT_COST",
		"TerrainType",
		"TERRAIN_TUNDRA"
	);
	
```

