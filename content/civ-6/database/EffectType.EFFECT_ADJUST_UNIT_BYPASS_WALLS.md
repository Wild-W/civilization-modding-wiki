---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_BYPASS_WALLS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_BYPASS_WALLS
>
> * Class: `UNITS`
> * Parameters:
>	* Enable `Boolean`

## Samples
```SQL {title="BYPASS_WALLS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"BYPASS_WALLS",
		"MODIFIER_PLAYER_UNIT_ADJUST_BYPASS_WALLS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"BYPASS_WALLS",
		"Enable",
		1
	);
	
```

