---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_SEE_HIDDEN
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_SEE_HIDDEN
>
> * Class: `UNITS`
> * Parameters:
>	* SeeHidden `Boolean`

## Samples
```SQL {title="UNIT_SEE_HIDDEN"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"UNIT_SEE_HIDDEN",
		"MODIFIER_PLAYER_UNIT_ADJUST_SEE_HIDDEN"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"UNIT_SEE_HIDDEN",
		"SeeHidden",
		1
	);
	
```

