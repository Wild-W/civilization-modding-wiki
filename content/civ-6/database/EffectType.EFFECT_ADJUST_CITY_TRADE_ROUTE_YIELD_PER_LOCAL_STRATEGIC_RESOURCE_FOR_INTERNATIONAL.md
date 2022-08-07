---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_TRADE_ROUTE_YIELD_PER_LOCAL_STRATEGIC_RESOURCE_FOR_INTERNATIONAL
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_TRADE_ROUTE_YIELD_PER_LOCAL_STRATEGIC_RESOURCE_FOR_INTERNATIONAL
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples
```SQL {title="TRAIT_FAITH_STRATEGIC_RESOURCES_TRADE_INTERNATIONAL"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_FAITH_STRATEGIC_RESOURCES_TRADE_INTERNATIONAL",
		"MODIFIER_PLAYER_CITIES_TRADE_ROUTE_YIELD_PER_LOCAL_STRATEGIC_RESOURCE_FOR_INTERNATIONAL"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_FAITH_STRATEGIC_RESOURCES_TRADE_INTERNATIONAL",
		"Amount",
		"0.5"
	),
	(
		"TRAIT_FAITH_STRATEGIC_RESOURCES_TRADE_INTERNATIONAL",
		"YieldType",
		"YIELD_FAITH"
	);
	
```

