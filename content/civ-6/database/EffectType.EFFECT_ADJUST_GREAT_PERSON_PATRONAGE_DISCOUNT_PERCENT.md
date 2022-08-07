---
tags:
- EffectType
title: EFFECT_ADJUST_GREAT_PERSON_PATRONAGE_DISCOUNT_PERCENT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_GREAT_PERSON_PATRONAGE_DISCOUNT_PERCENT
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples
```SQL {title="ORACLE_PATRONAGE_FAITH_DISCOUNT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"ORACLE_PATRONAGE_FAITH_DISCOUNT",
		"MODIFIER_PLAYER_ADJUST_GREAT_PERSON_PATRONAGE_DISCOUNT_PERCENT"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"ORACLE_PATRONAGE_FAITH_DISCOUNT",
		"Amount",
		25
	),
	(
		"ORACLE_PATRONAGE_FAITH_DISCOUNT",
		"YieldType",
		"YIELD_FAITH"
	);
	
```

