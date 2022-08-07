---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_OWNER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_OWNER
>
> * Class: `UNITS`
> * Parameters:
>	* NewOwner `String`

## Samples

```SQL {title="GREATPERSON_BOUDICA_ACTIVE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent,
		SubjectRequirementSetId
	)
VALUES
	(
		"GREATPERSON_BOUDICA_ACTIVE",
		"MODIFIER_PLAYER_UNITS_ADJUST_OWNER",
		1,
		1,
		"GREATPERSON_BOUDICA_ACTIVE_REQUIREMENTS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"GREATPERSON_BOUDICA_ACTIVE",
		"NewOwner",
		"Player"
	);
	
```

