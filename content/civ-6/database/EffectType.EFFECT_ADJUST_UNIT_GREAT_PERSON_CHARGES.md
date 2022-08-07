---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_GREAT_PERSON_CHARGES
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_GREAT_PERSON_CHARGES
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="HALICARNASSUS_ADJUST_ENGINEER_CHARGES"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"HALICARNASSUS_ADJUST_ENGINEER_CHARGES",
		"MODIFIER_PLAYER_UNITS_ADJUST_GREAT_PERSON_CHARGES",
		"UNIT_IS_ENGINEER"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"HALICARNASSUS_ADJUST_ENGINEER_CHARGES",
		"Amount",
		1
	);
	
```

