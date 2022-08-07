---
tags:
- EffectType
title: EFFECT_ADJUST_TRADE_ROUTE_YIELD_PER_SPECIALTY_DISTRICT_FOR_DOMESTIC
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_TRADE_ROUTE_YIELD_PER_SPECIALTY_DISTRICT_FOR_DOMESTIC
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples

```SQL {title="GREATPERSON_DOMESTIC_ROUTE_GOLD_PER_SPECIALTY_DISTRICT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent
	)
VALUES
	(
		"GREATPERSON_DOMESTIC_ROUTE_GOLD_PER_SPECIALTY_DISTRICT",
		"MODIFIER_PLAYER_ADJUST_TRADE_ROUTE_YIELD_PER_SPECIALTY_DISTRICT_FOR_DOMESTIC",
		1,
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
		"GREATPERSON_DOMESTIC_ROUTE_GOLD_PER_SPECIALTY_DISTRICT",
		"Amount",
		"0.5"
	),
	(
		"GREATPERSON_DOMESTIC_ROUTE_GOLD_PER_SPECIALTY_DISTRICT",
		"YieldType",
		"YIELD_GOLD"
	);
	
```

