---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_STATE_TRADE_ROUTE_DISTRICT_YIELD
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_STATE_TRADE_ROUTE_DISTRICT_YIELD
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples
```SQL {title="MINOR_CIV_KUMASI_CULTURE_TRADE_ROUTE_YIELD_BONUS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"MINOR_CIV_KUMASI_CULTURE_TRADE_ROUTE_YIELD_BONUS",
		"MODIFIER_PLAYER_CITIES_ADJUST_CITY_STATE_TRADE_ROUTE_DISTRICT_YIELD"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"MINOR_CIV_KUMASI_CULTURE_TRADE_ROUTE_YIELD_BONUS",
		"Amount",
		2
	),
	(
		"MINOR_CIV_KUMASI_CULTURE_TRADE_ROUTE_YIELD_BONUS",
		"YieldType",
		"YIELD_CULTURE"
	);
	
```

