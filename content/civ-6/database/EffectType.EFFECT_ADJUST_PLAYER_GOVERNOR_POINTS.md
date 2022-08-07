---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_GOVERNOR_POINTS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_GOVERNOR_POINTS
>
> * Class: `PLAYERS`
> * Parameters:
>	* Delta `Integer`

## Samples

```SQL {title="CONTRATACION_GOVERNOR_POINTS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce
	)
VALUES
	(
		"CONTRATACION_GOVERNOR_POINTS",
		"MODIFIER_PLAYER_ADJUST_GOVERNOR_POINTS",
		1
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"CONTRATACION_GOVERNOR_POINTS",
		"Delta",
		3
	);
	
```

