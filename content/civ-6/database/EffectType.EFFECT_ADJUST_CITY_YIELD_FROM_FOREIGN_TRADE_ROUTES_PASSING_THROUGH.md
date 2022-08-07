---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_YIELD_FROM_FOREIGN_TRADE_ROUTES_PASSING_THROUGH
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_YIELD_FROM_FOREIGN_TRADE_ROUTES_PASSING_THROUGH
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples
```SQL {title="FOREIGN_EXCHANGE_GOLD_FROM_FOREIGN_TRADE_PASSING_THROUGH"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"FOREIGN_EXCHANGE_GOLD_FROM_FOREIGN_TRADE_PASSING_THROUGH",
		"MODIFIER_CITY_ADJUST_YIELD_FROM_FOREIGN_TRADE_ROUTES_PASSING_THROUGH"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"FOREIGN_EXCHANGE_GOLD_FROM_FOREIGN_TRADE_PASSING_THROUGH",
		"Amount",
		3
	),
	(
		"FOREIGN_EXCHANGE_GOLD_FROM_FOREIGN_TRADE_PASSING_THROUGH",
		"YieldType",
		"YIELD_GOLD"
	);
	
```

