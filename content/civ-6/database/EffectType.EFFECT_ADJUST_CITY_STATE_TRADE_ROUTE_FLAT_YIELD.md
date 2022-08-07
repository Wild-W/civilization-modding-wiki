---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_STATE_TRADE_ROUTE_FLAT_YIELD
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_STATE_TRADE_ROUTE_FLAT_YIELD
>
> * Class: `Unknown`
> * Parameters:
>	* Amount `Unknown`
>	* YieldType `Unknown`

## Samples

```SQL {title="RAJ_CITY_TRADE_ROUTE_GOLD"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"RAJ_CITY_TRADE_ROUTE_GOLD",
		"MODIFIER_PLAYER_ADJUST_TRADE_ROUTES_CITY_STATE_YIELD"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"RAJ_CITY_TRADE_ROUTE_GOLD",
		"Amount",
		2
	),
	(
		"RAJ_CITY_TRADE_ROUTE_GOLD",
		"YieldType",
		"YIELD_GOLD"
	);
	
```

