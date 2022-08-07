---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_TRADE_ROUTE_ORIGIN_YIELD_FOR_ALLY_ROUTE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_TRADE_ROUTE_ORIGIN_YIELD_FOR_ALLY_ROUTE
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples

```SQL {title="ARSENALOFDEMOCRACY_TRADEROUTEFOODFROMALLY"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"ARSENALOFDEMOCRACY_TRADEROUTEFOODFROMALLY",
		"MODIFIER_PLAYER_ADJUST_TRADE_ROUTE_ORIGIN_YIELD_FOR_ALLY_ROUTE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"ARSENALOFDEMOCRACY_TRADEROUTEFOODFROMALLY",
		"Amount",
		4
	),
	(
		"ARSENALOFDEMOCRACY_TRADEROUTEFOODFROMALLY",
		"YieldType",
		"YIELD_FOOD"
	);
	
```

