---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_MOVE_AND_ATTACK
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_MOVE_AND_ATTACK
>
> * Class: `UNITS`
> * Parameters:
>	* CanAttack `Boolean`

## Samples

```SQL {title="NOMOVEANDSHOOT_MOVE_AND_ATTACK"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"NOMOVEANDSHOOT_MOVE_AND_ATTACK",
		"MODIFIER_PLAYER_UNIT_ADJUST_MOVE_AND_ATTACK"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"NOMOVEANDSHOOT_MOVE_AND_ATTACK",
		"CanAttack",
		0
	);
	
```

