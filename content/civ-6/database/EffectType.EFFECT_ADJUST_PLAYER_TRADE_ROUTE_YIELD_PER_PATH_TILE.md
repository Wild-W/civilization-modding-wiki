---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_TRADE_ROUTE_YIELD_PER_PATH_TILE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_TRADE_ROUTE_YIELD_PER_PATH_TILE
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples
```SQL {title="MINOR_CIV_HUNZA_GOLD_FROM_TRADE_ROUTE_LENGTH"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"MINOR_CIV_HUNZA_GOLD_FROM_TRADE_ROUTE_LENGTH",
		"MODIFIER_PLAYER_ADJUST_TRADE_ROUTE_YIELD_PER_PATH_TILE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"MINOR_CIV_HUNZA_GOLD_FROM_TRADE_ROUTE_LENGTH",
		"Amount",
		"0.2"
	),
	(
		"MINOR_CIV_HUNZA_GOLD_FROM_TRADE_ROUTE_LENGTH",
		"YieldType",
		"YIELD_GOLD"
	);
	
```

