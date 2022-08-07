---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_IGNORE_SHORES
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_IGNORE_SHORES
>
> * Class: `UNITS`
> * Parameters:
>	* Ignore `Boolean`

## Samples
```SQL {title="REDCOAT_DISEMBARK"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"REDCOAT_DISEMBARK",
		"MODIFIER_PLAYER_UNIT_ADJUST_IGNORE_SHORES"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"REDCOAT_DISEMBARK",
		"Ignore",
		1
	);
	
```

