---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_TRADE_ROUTE_YIELD_FOR_DOMESTIC
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_TRADE_ROUTE_YIELD_FOR_DOMESTIC
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples

```SQL {title="SUKIENNICE_DOMESTICGOLD"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"SUKIENNICE_DOMESTICGOLD",
		"MODIFIER_SINGLE_CITY_ADJUST_TRADE_ROUTE_YIELD_FOR_DOMESTIC"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"SUKIENNICE_DOMESTICGOLD",
		"Amount",
		4
	),
	(
		"SUKIENNICE_DOMESTICGOLD",
		"YieldType",
		"YIELD_GOLD"
	);
	
```

