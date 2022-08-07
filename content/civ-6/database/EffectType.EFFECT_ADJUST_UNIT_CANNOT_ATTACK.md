---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_CANNOT_ATTACK
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_CANNOT_ATTACK
>
> * Class: `UNITS`
> * Parameters:
>	* Disable `Boolean`

## Samples
```SQL {title="CANNOT_ATTACK"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"CANNOT_ATTACK",
		"MODIFIER_PLAYER_UNIT_ADJUST_CANNOT_ATTACK"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"CANNOT_ATTACK",
		"Disable",
		1
	);
	
```

