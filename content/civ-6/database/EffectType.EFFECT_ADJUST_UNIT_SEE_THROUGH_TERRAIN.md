---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_SEE_THROUGH_TERRAIN
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_SEE_THROUGH_TERRAIN
>
> * Class: `UNITS`
> * Parameters:
>	* CanSee `Boolean`

## Samples

```SQL {title="UNOBSTRUCTED_VIEW_TERRAIN"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"UNOBSTRUCTED_VIEW_TERRAIN",
		"MODIFIER_PLAYER_UNIT_ADJUST_SEE_THROUGH_TERRAIN"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"UNOBSTRUCTED_VIEW_TERRAIN",
		"CanSee",
		1
	);
	
```

