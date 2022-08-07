---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_SPY_OPERATION_TIME
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_SPY_OPERATION_TIME
>
> * Class: `UNITS`
> * Parameters:
>	* OperationType `String`
>		* [UnitOperations.OperationType]
>	* ReductionPercent `Integer`

## Samples
```SQL {title="SPY_LINGUIST_ROCKETRYTIME"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"SPY_LINGUIST_ROCKETRYTIME",
		"MODIFIER_PLAYER_UNIT_ADJUST_SPY_OPERATION_TIME"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"SPY_LINGUIST_ROCKETRYTIME",
		"OperationType",
		"UNITOPERATION_SPY_DISRUPT_ROCKETRY"
	),
	(
		"SPY_LINGUIST_ROCKETRYTIME",
		"ReductionPercent",
		25
	);
	
```

