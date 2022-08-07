---
tags:
- EffectType
title: EFFECT_ADJUST_TRADE_ROUTE_YIELD_FROM_OTHERS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_TRADE_ROUTE_YIELD_FROM_OTHERS
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`
>	* Domestic `Boolean`
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples
```SQL {title="GREATPERSON_GOLD_FROM_INCOMING_FOREIGN_ROUTES"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent
	)
VALUES
	(
		"GREATPERSON_GOLD_FROM_INCOMING_FOREIGN_ROUTES",
		"MODIFIER_SINGLE_CITY_ADJUST_TRADE_ROUTE_YIELD_FROM_OTHERS",
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
		"GREATPERSON_GOLD_FROM_INCOMING_FOREIGN_ROUTES",
		"Amount",
		2
	),
	(
		"GREATPERSON_GOLD_FROM_INCOMING_FOREIGN_ROUTES",
		"YieldType",
		"YIELD_GOLD"
	);
	
```

```SQL {title="SANKORE_TRADE_GAIN_SCIENCE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"SANKORE_TRADE_GAIN_SCIENCE",
		"MODIFIER_SINGLE_CITY_ADJUST_TRADE_ROUTE_YIELD_FROM_OTHERS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"SANKORE_TRADE_GAIN_SCIENCE",
		"Amount",
		2
	),
	(
		"SANKORE_TRADE_GAIN_SCIENCE",
		"Domestic",
		0
	),
	(
		"SANKORE_TRADE_GAIN_SCIENCE",
		"YieldType",
		"YIELD_SCIENCE"
	);
	
```

