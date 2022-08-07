---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_YIELD_PER_MAJOR_TRADE_PARTNER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_YIELD_PER_MAJOR_TRADE_PARTNER
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples

```SQL {title="MINOR_CIV_SINGAPORE_PRODUCTION_PER_MAJOR_TRADE_PARTNER"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"MINOR_CIV_SINGAPORE_PRODUCTION_PER_MAJOR_TRADE_PARTNER",
		"MODIFIER_PLAYER_CITIES_ADJUST_CITY_YIELD_PER_MAJOR_TRADE_PARTNER"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"MINOR_CIV_SINGAPORE_PRODUCTION_PER_MAJOR_TRADE_PARTNER",
		"Amount",
		2
	),
	(
		"MINOR_CIV_SINGAPORE_PRODUCTION_PER_MAJOR_TRADE_PARTNER",
		"YieldType",
		"YIELD_PRODUCTION"
	);
	
```

