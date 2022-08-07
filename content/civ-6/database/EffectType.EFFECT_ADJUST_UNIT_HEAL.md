---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_HEAL
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_HEAL
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="GOODY_MILITARY_HEAL"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent
	)
VALUES
	(
		"GOODY_MILITARY_HEAL",
		"MODIFIER_PLAYER_UNIT_ADJUST_HEAL",
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
		"GOODY_MILITARY_HEAL",
		"Amount",
		100
	);
	
```

