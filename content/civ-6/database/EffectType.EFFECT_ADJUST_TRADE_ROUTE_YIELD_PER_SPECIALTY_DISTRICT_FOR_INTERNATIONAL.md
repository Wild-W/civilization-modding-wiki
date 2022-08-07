---
tags:
- EffectType
title: EFFECT_ADJUST_TRADE_ROUTE_YIELD_PER_SPECIALTY_DISTRICT_FOR_INTERNATIONAL
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_TRADE_ROUTE_YIELD_PER_SPECIALTY_DISTRICT_FOR_INTERNATIONAL
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples

```SQL {title="COMMEMORATION_ECONOMIC_GA_TRADE_ROUTE_YIELDS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		OwnerRequirementSetId
	)
VALUES
	(
		"COMMEMORATION_ECONOMIC_GA_TRADE_ROUTE_YIELDS",
		"MODIFIER_PLAYER_ADJUST_TRADE_ROUTE_YIELD_PER_SPECIALTY_DISTRICT_FOR_INTERNATIONAL",
		"PLAYER_HAS_GOLDEN_AGE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"COMMEMORATION_ECONOMIC_GA_TRADE_ROUTE_YIELDS",
		"Amount",
		3
	),
	(
		"COMMEMORATION_ECONOMIC_GA_TRADE_ROUTE_YIELDS",
		"YieldType",
		"YIELD_GOLD"
	);
	
```

