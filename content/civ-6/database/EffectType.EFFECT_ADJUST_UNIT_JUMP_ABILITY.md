---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_JUMP_ABILITY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_JUMP_ABILITY
>
> * Class: `UNITS`
> * Parameters:
>	* Range `Integer`

## Samples

```SQL {title="GDR_JUMP_ABILITY"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"GDR_JUMP_ABILITY",
		"MODIFIER_SINGLE_UNIT_ADJUST_JUMP_DISTANCE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"GDR_JUMP_ABILITY",
		"Range",
		5
	);
	
```

