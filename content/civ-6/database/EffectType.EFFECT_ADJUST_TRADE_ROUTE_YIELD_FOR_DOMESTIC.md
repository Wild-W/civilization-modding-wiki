---
tags:
- EffectType
title: EFFECT_ADJUST_TRADE_ROUTE_YIELD_FOR_DOMESTIC
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_TRADE_ROUTE_YIELD_FOR_DOMESTIC
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`
>	* Intercontinental `Boolean`
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples

```SQL {title="TRAIT_DOMESTIC_FAITH"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_DOMESTIC_FAITH",
		"MODIFIER_PLAYER_ADJUST_TRADE_ROUTE_YIELD_FOR_DOMESTIC"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_DOMESTIC_FAITH",
		"Amount",
		2
	),
	(
		"TRAIT_DOMESTIC_FAITH",
		"YieldType",
		"YIELD_FAITH"
	);
	
```


```SQL {title="TRAIT_INTERCONTINENTAL_DOMESTIC_FAITH"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_INTERCONTINENTAL_DOMESTIC_FAITH",
		"MODIFIER_PLAYER_ADJUST_TRADE_ROUTE_YIELD_FOR_DOMESTIC"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_INTERCONTINENTAL_DOMESTIC_FAITH",
		"Amount",
		4
	),
	(
		"TRAIT_INTERCONTINENTAL_DOMESTIC_FAITH",
		"Intercontinental",
		1
	),
	(
		"TRAIT_INTERCONTINENTAL_DOMESTIC_FAITH",
		"YieldType",
		"YIELD_FAITH"
	);
	
```
