---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_TRADE_ROUTE_YIELD_PER_DESTINATION_STRATEGIC_RESOURCE_FOR_INTERNATIONAL
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_TRADE_ROUTE_YIELD_PER_DESTINATION_STRATEGIC_RESOURCE_FOR_INTERNATIONAL
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples

```SQL {title="GREATPERSON_INTERNATIONAL_ROUTE_GOLD_PER_STRATEGIC"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		Permanent
	)
VALUES
	(
		"GREATPERSON_INTERNATIONAL_ROUTE_GOLD_PER_STRATEGIC",
		"MODIFIER_PLAYER_CITIES_ADJUST_TRADE_ROUTE_YIELD_PER_DESTINATION_STRATEGIC_FOR_INTERNATIONAL",
		1
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"GREATPERSON_INTERNATIONAL_ROUTE_GOLD_PER_STRATEGIC",
		"Amount",
		2
	),
	(
		"GREATPERSON_INTERNATIONAL_ROUTE_GOLD_PER_STRATEGIC",
		"YieldType",
		"YIELD_GOLD"
	);
	
```

