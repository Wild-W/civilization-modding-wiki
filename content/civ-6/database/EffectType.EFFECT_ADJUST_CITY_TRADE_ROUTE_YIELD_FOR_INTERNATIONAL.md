---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_TRADE_ROUTE_YIELD_FOR_INTERNATIONAL
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_TRADE_ROUTE_YIELD_FOR_INTERNATIONAL
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples
```SQL {title="SUKIENNICE_INTERNATIONALPRODUCTION"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"SUKIENNICE_INTERNATIONALPRODUCTION",
		"MODIFIER_SINGLE_CITY_ADJUST_TRADE_ROUTE_YIELD_FOR_INTERNATIONAL"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"SUKIENNICE_INTERNATIONALPRODUCTION",
		"Amount",
		2
	),
	(
		"SUKIENNICE_INTERNATIONALPRODUCTION",
		"YieldType",
		"YIELD_PRODUCTION"
	);
	
```

