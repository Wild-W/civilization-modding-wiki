---
tags:
- EffectType
title: EFFECT_ADJUST_GREAT_WORK_OBJECT_NO_TOURISM
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_GREAT_WORK_OBJECT_NO_TOURISM
>
> * Class: `Unknown`
> * Parameters:
>	* NoTourism `Boolean`

## Samples

```SQL {title="NO_TOURISM_FROM_GREAT_WORK_OBJECT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"NO_TOURISM_FROM_GREAT_WORK_OBJECT",
		"MODIFIER_PLAYER_ADJUST_GREAT_WORK_OBJECT_NO_TOURISM"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"NO_TOURISM_FROM_GREAT_WORK_OBJECT",
		"NoTourism",
		1
	);
	
```

