---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_PER_UNUSED_MOVEMENT_COMBAT_BONUS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_PER_UNUSED_MOVEMENT_COMBAT_BONUS
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="CAROLEAN_UNUSED_MOVEMENT_COMBAT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"CAROLEAN_UNUSED_MOVEMENT_COMBAT",
		"MODIFIER_SINGLE_UNIT_ADJUST_COMBAT_FOR_UNUSED_MOVEMENT"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"CAROLEAN_UNUSED_MOVEMENT_COMBAT",
		"Amount",
		3
	);
	
```

