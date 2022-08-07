---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_SEE_THROUGH_FEATURES
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_SEE_THROUGH_FEATURES
>
> * Class: `UNITS`
> * Parameters:
>	* CanSee `Boolean`

## Samples
```SQL {title="UNOBSTRUCTED_VIEW"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"UNOBSTRUCTED_VIEW",
		"MODIFIER_PLAYER_UNIT_ADJUST_SEE_THROUGH_FEATURES"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"UNOBSTRUCTED_VIEW",
		"CanSee",
		1
	);
	
```

