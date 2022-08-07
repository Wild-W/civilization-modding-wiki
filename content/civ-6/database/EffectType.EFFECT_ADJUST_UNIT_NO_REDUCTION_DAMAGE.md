---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_NO_REDUCTION_DAMAGE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_NO_REDUCTION_DAMAGE
>
> * Class: `UNITS`
> * Parameters:
>	* NoReduction `Boolean`

## Samples

```SQL {title="SAMURAI_NO_REDUCTION_DAMAGE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"SAMURAI_NO_REDUCTION_DAMAGE",
		"MODIFIER_PLAYER_UNIT_ADJUST_NO_REDUCTION_DAMAGE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"SAMURAI_NO_REDUCTION_DAMAGE",
		"NoReduction",
		1
	);
	
```

