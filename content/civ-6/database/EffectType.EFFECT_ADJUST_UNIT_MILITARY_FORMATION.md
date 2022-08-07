---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_MILITARY_FORMATION
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_MILITARY_FORMATION
>
> * Class: `UNITS`
> * Parameters:
>	* MilitaryFormationType `String`
>		* ARMY_MILITARY_FORMATION>		  CORPS_MILITARY_FORMATION

## Samples
```SQL {title="GREATPERSON_GAIUS_DUILIUS_ACTIVE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent
	)
VALUES
	(
		"GREATPERSON_GAIUS_DUILIUS_ACTIVE",
		"MODIFIER_PLAYER_UNIT_ADJUST_MILITARY_FORMATION",
		1,
		1
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"GREATPERSON_GAIUS_DUILIUS_ACTIVE",
		"MilitaryFormationType",
		"CORPS_MILITARY_FORMATION"
	);
	
```

