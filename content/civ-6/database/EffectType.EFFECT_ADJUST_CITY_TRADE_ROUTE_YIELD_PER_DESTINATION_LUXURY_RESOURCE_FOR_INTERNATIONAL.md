---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_TRADE_ROUTE_YIELD_PER_DESTINATION_LUXURY_RESOURCE_FOR_INTERNATIONAL
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_TRADE_ROUTE_YIELD_PER_DESTINATION_LUXURY_RESOURCE_FOR_INTERNATIONAL
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples

```SQL {title="MINOR_CIV_AMSTERDAM_LUXURY_TRADE_ROUTE_BONUS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"MINOR_CIV_AMSTERDAM_LUXURY_TRADE_ROUTE_BONUS",
		"MODIFIER_PLAYER_CITIES_ADJUST_TRADE_ROUTE_YIELD_PER_DESTINATION_LUXURY_FOR_INTERNATIONAL"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"MINOR_CIV_AMSTERDAM_LUXURY_TRADE_ROUTE_BONUS",
		"Amount",
		1
	),
	(
		"MINOR_CIV_AMSTERDAM_LUXURY_TRADE_ROUTE_BONUS",
		"YieldType",
		"YIELD_GOLD"
	);
	
```
