---
tags:
- EffectType
title: EFFECT_ADJUST_TRADE_ROUTE_YIELD_TO_OTHERS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_TRADE_ROUTE_YIELD_TO_OTHERS
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`
>	* Domestic `Boolean`
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples

```SQL {title="GREATPERSON_GOLD_TO_INCOMING_FOREIGN_ROUTES"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent
	)
VALUES
	(
		"GREATPERSON_GOLD_TO_INCOMING_FOREIGN_ROUTES",
		"MODIFIER_SINGLE_CITY_ADJUST_TRADE_ROUTE_YIELD_TO_OTHERS",
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
		"GREATPERSON_GOLD_TO_INCOMING_FOREIGN_ROUTES",
		"Amount",
		2
	),
	(
		"GREATPERSON_GOLD_TO_INCOMING_FOREIGN_ROUTES",
		"YieldType",
		"YIELD_GOLD"
	);
	
```


```SQL {title="SURPLUS_LOGISTICS_TRADE_ROUTE_FOOD"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"SURPLUS_LOGISTICS_TRADE_ROUTE_FOOD",
		"MODIFIER_SINGLE_CITY_ADJUST_TRADE_ROUTE_YIELD_TO_OTHERS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"SURPLUS_LOGISTICS_TRADE_ROUTE_FOOD",
		"Amount",
		2
	),
	(
		"SURPLUS_LOGISTICS_TRADE_ROUTE_FOOD",
		"Domestic",
		1
	),
	(
		"SURPLUS_LOGISTICS_TRADE_ROUTE_FOOD",
		"YieldType",
		"YIELD_FOOD"
	);
	
```

