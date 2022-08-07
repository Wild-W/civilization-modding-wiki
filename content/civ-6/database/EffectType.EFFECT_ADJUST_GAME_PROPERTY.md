---
tags:
- EffectType
title: EFFECT_ADJUST_GAME_PROPERTY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_GAME_PROPERTY
>
> * Class: `Unknown`
> * Parameters:
>	* Amount `Unknown`
>	* Key `Unknown`

## Samples
```SQL {title="TOWERDEFENSE_INCREMENT_ZOMBIE_DEATHS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		Permanent,
		SubjectRequirementSetId
	)
VALUES
	(
		"TOWERDEFENSE_INCREMENT_ZOMBIE_DEATHS",
		"MODIFIER_ALL_UNIT_DEATHS_ADJUST_GAME_PROPERTY",
		1,
		"DID_ZOMBIE_DIE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TOWERDEFENSE_INCREMENT_ZOMBIE_DEATHS",
		"Amount",
		1
	),
	(
		"TOWERDEFENSE_INCREMENT_ZOMBIE_DEATHS",
		"Key",
		"GAME_NUMBER_OF_ZOMBIE_DEATHS"
	);
	
```

