---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_NUM_ATTACKS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_NUM_ATTACKS
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="ELITE_GUARD_ADDITIONAL_ATTACK"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"ELITE_GUARD_ADDITIONAL_ATTACK",
		"MODIFIER_UNIT_ADJUST_NUM_ATTACKS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"ELITE_GUARD_ADDITIONAL_ATTACK",
		"Amount",
		1
	);
	
```

