---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_TRADE_ROUTE_YIELD_PER_TERRAIN_FOR_INTERNATIONAL
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_TRADE_ROUTE_YIELD_PER_TERRAIN_FOR_INTERNATIONAL
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`
>	* Origin `Boolean`
>	* TerrainType `String`
>	* YieldType `String`

## Samples

```SQL {title="TRADE_ROUTE_GOLD_DESERT_ORIGIN"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRADE_ROUTE_GOLD_DESERT_ORIGIN",
		"MODIFIER_PLAYER_ADJUST_TRADE_ROUTE_YIELD_PER_TERRAIN_INTERNATIONAL"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRADE_ROUTE_GOLD_DESERT_ORIGIN",
		"Amount",
		1
	),
	(
		"TRADE_ROUTE_GOLD_DESERT_ORIGIN",
		"Origin",
		1
	),
	(
		"TRADE_ROUTE_GOLD_DESERT_ORIGIN",
		"TerrainType",
		"TERRAIN_DESERT"
	),
	(
		"TRADE_ROUTE_GOLD_DESERT_ORIGIN",
		"YieldType",
		"YIELD_GOLD"
	);
	
```

