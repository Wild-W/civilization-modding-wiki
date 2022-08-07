---
tags:
- EffectType
title: EFFECT_ADJUST_DISABLE_INFLUENCE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_DISABLE_INFLUENCE
>
> * Class: `PLAYERS`
> * Parameters:
>	* Disable `Boolean`

## Samples
```SQL {title="ROGUESTATE_DISABLE_INFLUENCE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"ROGUESTATE_DISABLE_INFLUENCE",
		"MODIFIER_PLAYER_DISABLE_INFLUENCE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"ROGUESTATE_DISABLE_INFLUENCE",
		"Disable",
		1
	);
	
```

