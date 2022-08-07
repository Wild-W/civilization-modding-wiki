---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_ATTACK_RANGE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_ATTACK_RANGE
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="RECEIVE_RANGE_BONUS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"RECEIVE_RANGE_BONUS",
		"MODIFIER_UNIT_ADJUST_ATTACK_RANGE",
		"RANGE_BONUS_REQUIREMENTS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"RECEIVE_RANGE_BONUS",
		"Amount",
		1
	);
	
```

