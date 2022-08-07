---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_IGNORE_RIVERS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_IGNORE_RIVERS
>
> * Class: `UNITS`
> * Parameters:
>	* Ignore `Boolean`

## Samples

```SQL {title="MOD_IGNORE_CROSSING_RIVERS_COST"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"MOD_IGNORE_CROSSING_RIVERS_COST",
		"MODIFIER_PLAYER_UNIT_ADJUST_IGNORE_RIVERS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"MOD_IGNORE_CROSSING_RIVERS_COST",
		"Ignore",
		1
	);
	
```

