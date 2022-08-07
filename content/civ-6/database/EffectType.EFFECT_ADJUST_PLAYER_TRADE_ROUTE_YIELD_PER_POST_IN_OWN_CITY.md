---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_TRADE_ROUTE_YIELD_PER_POST_IN_OWN_CITY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_TRADE_ROUTE_YIELD_PER_POST_IN_OWN_CITY
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples

```SQL {title="TRAIT_GOLD_FROM_DOMESTIC_TRADING_POSTS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_GOLD_FROM_DOMESTIC_TRADING_POSTS",
		"MODIFIER_PLAYER_ADJUST_TRADE_ROUTE_YIELD_PER_POST_IN_OWN_CITY"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_GOLD_FROM_DOMESTIC_TRADING_POSTS",
		"Amount",
		1
	),
	(
		"TRAIT_GOLD_FROM_DOMESTIC_TRADING_POSTS",
		"YieldType",
		"YIELD_GOLD"
	);
	
```

