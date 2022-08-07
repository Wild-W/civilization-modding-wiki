---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_ENABLE_WALL_ATTACK
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_ENABLE_WALL_ATTACK
>
> * Class: `UNITS`
> * Parameters:
>	* Enable `Boolean`

## Samples

```SQL {title="ENABLE_WALL_ATTACK"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"ENABLE_WALL_ATTACK",
		"MODIFIER_PLAYER_UNIT_ADJUST_ENABLE_WALL_ATTACK"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"ENABLE_WALL_ATTACK",
		"Enable",
		1
	);
	
```

