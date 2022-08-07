---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_TRADE_ROUTE_YIELD_PER_IMPROVEMENT_IN_TARGET_CITY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_TRADE_ROUTE_YIELD_PER_IMPROVEMENT_IN_TARGET_CITY
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`
>	* Destination `Boolean`
>	* ImprovementType `String`
>		* [Improvements.ImprovementType]
>	* Origin `Boolean`
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples

```SQL {title="TRAIT_TRADE_FOOD_FROM_CAMPS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_TRADE_FOOD_FROM_CAMPS",
		"MODIFIER_PLAYER_ADJUST_TRADE_ROUTE_YIELD_PER_IMPROVEMENT_IN_TARGET"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_TRADE_FOOD_FROM_CAMPS",
		"Amount",
		1
	),
	(
		"TRAIT_TRADE_FOOD_FROM_CAMPS",
		"ImprovementType",
		"IMPROVEMENT_CAMP"
	),
	(
		"TRAIT_TRADE_FOOD_FROM_CAMPS",
		"Origin",
		1
	),
	(
		"TRAIT_TRADE_FOOD_FROM_CAMPS",
		"YieldType",
		"YIELD_FOOD"
	);
	
```


```SQL {title="TRAIT_TRADE_GOLD_FROM_CAMPS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_TRADE_GOLD_FROM_CAMPS",
		"MODIFIER_PLAYER_ADJUST_TRADE_ROUTE_YIELD_PER_IMPROVEMENT_IN_TARGET"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_TRADE_GOLD_FROM_CAMPS",
		"Amount",
		1
	),
	(
		"TRAIT_TRADE_GOLD_FROM_CAMPS",
		"Destination",
		1
	),
	(
		"TRAIT_TRADE_GOLD_FROM_CAMPS",
		"ImprovementType",
		"IMPROVEMENT_CAMP"
	),
	(
		"TRAIT_TRADE_GOLD_FROM_CAMPS",
		"YieldType",
		"YIELD_GOLD"
	);
	
```

