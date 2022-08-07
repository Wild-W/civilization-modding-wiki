---
tags:
- EffectType
title: EFFECT_ADJUST_TRADE_ROUTE_YIELD
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_TRADE_ROUTE_YIELD
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples
```SQL {title="CARAVANSARIES_TRADEROUTEGOLD"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"CARAVANSARIES_TRADEROUTEGOLD",
		"MODIFIER_PLAYER_ADJUST_TRADE_ROUTE_YIELD"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"CARAVANSARIES_TRADEROUTEGOLD",
		"Amount",
		2
	),
	(
		"CARAVANSARIES_TRADEROUTEGOLD",
		"YieldType",
		"YIELD_GOLD"
	);
	
```

