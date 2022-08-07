---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_IGNORE_TERRAIN_COST
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_IGNORE_TERRAIN_COST
>
> * Class: `UNITS`
> * Parameters:
>	* Ignore `Boolean`
>	* Type `String`

## Samples

```SQL {title="MOD_IGNORE_TERRAIN_COST"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"MOD_IGNORE_TERRAIN_COST",
		"MODIFIER_PLAYER_UNIT_ADJUST_IGNORE_TERRAIN_COST"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"MOD_IGNORE_TERRAIN_COST",
		"Ignore",
		1
	),
	(
		"MOD_IGNORE_TERRAIN_COST",
		"Type",
		"ALL"
	);
	
```

