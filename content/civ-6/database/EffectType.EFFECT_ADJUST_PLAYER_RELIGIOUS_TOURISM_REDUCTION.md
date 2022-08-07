---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_RELIGIOUS_TOURISM_REDUCTION
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_RELIGIOUS_TOURISM_REDUCTION
>
> * Class: `PLAYERS`
> * Parameters:
>	* Modifier `Integer`
>		* [Modifiers.ModifierId]

## Samples
```SQL {title="CIVIC_REDUCE_RELIGIOUS_TOURISM"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"CIVIC_REDUCE_RELIGIOUS_TOURISM",
		"MODIFIER_PLAYER_ADJUST_RELIGIOUS_TOURISM_REDUCTION"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"CIVIC_REDUCE_RELIGIOUS_TOURISM",
		"Modifier",
		50
	);
	
```

