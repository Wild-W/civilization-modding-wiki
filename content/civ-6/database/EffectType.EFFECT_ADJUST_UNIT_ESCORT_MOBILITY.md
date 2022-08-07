---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_ESCORT_MOBILITY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_ESCORT_MOBILITY
>
> * Class: `UNITS`
> * Parameters:
>	* EscortMobility `Boolean`

## Samples

```SQL {title="ESCORT_MOBILITY_SHARED_MOVEMENT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"ESCORT_MOBILITY_SHARED_MOVEMENT",
		"MODIFIER_UNIT_ADJUST_ESCORT_MOBILITY"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"ESCORT_MOBILITY_SHARED_MOVEMENT",
		"EscortMobility",
		1
	);
	
```

