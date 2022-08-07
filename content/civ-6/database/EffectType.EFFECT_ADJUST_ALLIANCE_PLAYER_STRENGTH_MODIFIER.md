---
tags:
- EffectType
title: EFFECT_ADJUST_ALLIANCE_PLAYER_STRENGTH_MODIFIER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_ALLIANCE_PLAYER_STRENGTH_MODIFIER
>
> * Class: `COMBATS`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="ALLIANCE_ADJUST_COMBAT_STRENGTH"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"ALLIANCE_ADJUST_COMBAT_STRENGTH",
		"MODIFIER_ALLIANCE_COMBATS_UNIT_STRENGTHS",
		"ALLIES_AT_WAR_WITH_TARGET_REQUIREMENTS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"ALLIANCE_ADJUST_COMBAT_STRENGTH",
		"Amount",
		5
	);
	
```

