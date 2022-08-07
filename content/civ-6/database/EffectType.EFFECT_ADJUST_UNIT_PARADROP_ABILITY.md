---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_PARADROP_ABILITY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_PARADROP_ABILITY
>
> * Class: `UNITS`
> * Parameters:
>	* CanDrop `Boolean`

## Samples
```SQL {title="SPEC_OPS_PARADROP_ABILITY"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"SPEC_OPS_PARADROP_ABILITY",
		"MODIFIER_PLAYER_UNIT_ADJUST_PARADROP_ABILITY"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"SPEC_OPS_PARADROP_ABILITY",
		"CanDrop",
		1
	);
	
```

