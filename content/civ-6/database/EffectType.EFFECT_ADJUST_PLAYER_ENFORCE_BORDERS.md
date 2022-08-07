---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_ENFORCE_BORDERS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_ENFORCE_BORDERS
>
> * Class: `PLAYERS`
> * Parameters:
>	* Enable `Boolean`

## Samples
```SQL {title="CIVIC_ENFORCE_BORDERS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"CIVIC_ENFORCE_BORDERS",
		"MODIFIER_PLAYER_ADJUST_ENFORCE_BORDERS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"CIVIC_ENFORCE_BORDERS",
		"Enable",
		1
	);
	
```

