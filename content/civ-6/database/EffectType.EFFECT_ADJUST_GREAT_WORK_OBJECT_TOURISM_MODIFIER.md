---
tags:
- EffectType
title: EFFECT_ADJUST_GREAT_WORK_OBJECT_TOURISM_MODIFIER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_GREAT_WORK_OBJECT_TOURISM_MODIFIER
>
> * Class: `Unknown`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="ADD_TOURISM_FROM_GREAT_WORK_OBJECT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"ADD_TOURISM_FROM_GREAT_WORK_OBJECT",
		"MODIFIER_PLAYER_ADJUST_GREAT_WORK_OBJECT_TOURISM"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"ADD_TOURISM_FROM_GREAT_WORK_OBJECT",
		"Amount",
		100
	);
	
```

