---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_SKIP_FREE_CITY_STEP
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_SKIP_FREE_CITY_STEP
>
> * Class: `PLAYERS`
> * Parameters:
>	* Skip `Boolean`

## Samples

```SQL {title="SKIP_FREE_CITY"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"SKIP_FREE_CITY",
		"MODIFIER_PLAYER_ADJUST_SKIP_FREE_CITY_STEP"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"SKIP_FREE_CITY",
		"Skip",
		1
	);
	
```

