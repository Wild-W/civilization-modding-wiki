---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_TRADE_ROUTE_YIELD_PER_TERRAIN_FOR_DOMESTIC
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_TRADE_ROUTE_YIELD_PER_TERRAIN_FOR_DOMESTIC
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`
>	* Origin `Boolean`
>	* TerrainType `String`
>	* YieldType `String`

## Samples

```SQL {title="DOMESTIC_TRADE_ROUTE_FOOD_GRASS_MOUNTAIN_ORIGIN"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"DOMESTIC_TRADE_ROUTE_FOOD_GRASS_MOUNTAIN_ORIGIN",
		"MODIFIER_PLAYER_ADJUST_TRADE_ROUTE_YIELD_PER_TERRAIN_DOMESTIC"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"DOMESTIC_TRADE_ROUTE_FOOD_GRASS_MOUNTAIN_ORIGIN",
		"Amount",
		1
	),
	(
		"DOMESTIC_TRADE_ROUTE_FOOD_GRASS_MOUNTAIN_ORIGIN",
		"Origin",
		1
	),
	(
		"DOMESTIC_TRADE_ROUTE_FOOD_GRASS_MOUNTAIN_ORIGIN",
		"TerrainType",
		"TERRAIN_GRASS_MOUNTAIN"
	),
	(
		"DOMESTIC_TRADE_ROUTE_FOOD_GRASS_MOUNTAIN_ORIGIN",
		"YieldType",
		"YIELD_FOOD"
	);
	
```

