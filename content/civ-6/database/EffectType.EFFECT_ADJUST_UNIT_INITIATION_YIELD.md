---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_INITIATION_YIELD
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_INITIATION_YIELD
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Integer`
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples

```SQL {title="APOSTLE_INITIATION_GOLD"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"APOSTLE_INITIATION_GOLD",
		"MODIFIER_PLAYER_UNIT_ADJUST_INITIATION_GOLD"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"APOSTLE_INITIATION_GOLD",
		"Amount",
		100
	),
	(
		"APOSTLE_INITIATION_GOLD",
		"YieldType",
		"YIELD_GOLD"
	);
	
```

