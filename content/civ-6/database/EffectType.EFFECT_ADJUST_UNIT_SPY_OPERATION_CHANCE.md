---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_SPY_OPERATION_CHANCE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_SPY_OPERATION_CHANCE
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Integer`
>	* Offensive `Boolean`
>	* OperationType `String`
>		* [UnitOperations.OperationType]

## Samples

```SQL {title="SPY_TECHNOLOGIST"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"SPY_TECHNOLOGIST",
		"MODIFIER_PLAYER_UNIT_ADJUST_SPY_OPERATION_CHANCE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"SPY_TECHNOLOGIST",
		"Amount",
		2
	),
	(
		"SPY_TECHNOLOGIST",
		"Offensive",
		1
	),
	(
		"SPY_TECHNOLOGIST",
		"OperationType",
		"UNITOPERATION_SPY_STEAL_TECH_BOOST"
	);
	
```

