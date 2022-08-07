---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_TRADE_ROUTE_YIELD_PER_POST_IN_FOREIGN_CITY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_TRADE_ROUTE_YIELD_PER_POST_IN_FOREIGN_CITY
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples
```SQL {title="MINOR_CIV_JAKARTA_TRADING_POST_BONUS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"MINOR_CIV_JAKARTA_TRADING_POST_BONUS",
		"MODIFIER_PLAYER_ADJUST_TRADE_ROUTE_YIELD_PER_POST_IN_FOREIGN_CITY"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"MINOR_CIV_JAKARTA_TRADING_POST_BONUS",
		"Amount",
		1
	),
	(
		"MINOR_CIV_JAKARTA_TRADING_POST_BONUS",
		"YieldType",
		"YIELD_GOLD"
	);
	
```

