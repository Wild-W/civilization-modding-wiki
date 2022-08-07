---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_TRADE_ROUTE_ORIGIN_YIELD_FOR_SUZERAIN_ROUTE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_TRADE_ROUTE_ORIGIN_YIELD_FOR_SUZERAIN_ROUTE
>
> * Class: `Unknown`
> * Parameters:
>	* Amount `Unknown`
>	* YieldType `Unknown`

## Samples
```SQL {title="WISSELBANKEN_TRADEROUTEFOODFROMSUZERAIN"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"WISSELBANKEN_TRADEROUTEFOODFROMSUZERAIN",
		"MODIFIER_PLAYER_ADJUST_TRADE_ROUTE_ORIGIN_YIELD_FOR_SUZERAIN_ROUTE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"WISSELBANKEN_TRADEROUTEFOODFROMSUZERAIN",
		"Amount",
		2
	),
	(
		"WISSELBANKEN_TRADEROUTEFOODFROMSUZERAIN",
		"YieldType",
		"YIELD_FOOD"
	);
	
```

