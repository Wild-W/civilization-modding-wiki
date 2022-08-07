---
tags:
- EffectType
title: EFFECT_ADJUST_DEFENDER_STRENGTH_MODIFIER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_DEFENDER_STRENGTH_MODIFIER
>
> * Class: `COMBATS`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="MILITARY_EMERGENCY_MEMBER_COMBAT_STRENGTH_ATTACK"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"MILITARY_EMERGENCY_MEMBER_COMBAT_STRENGTH_ATTACK",
		"MODIFIER_EMERGENCY_COMBATS_ADJUST_DEFENDER_STRENGTH",
		"MILITARY_EMERGENCY_COMBAT_STRENGTH_ATTACKER_REQUIREMENTS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"MILITARY_EMERGENCY_MEMBER_COMBAT_STRENGTH_ATTACK",
		"Amount",
		"-2"
	);
	
```

