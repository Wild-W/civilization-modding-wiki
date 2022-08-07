---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_IGNORE_CLIFF_WALLS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_IGNORE_CLIFF_WALLS
>
> * Class: `UNITS`
> * Parameters:
>	* Ignore `Boolean`

## Samples
```SQL {title="COMMANDO_BONUS_IGNORE_CLIFF_WALLS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"COMMANDO_BONUS_IGNORE_CLIFF_WALLS",
		"MODIFIER_PLAYER_UNIT_ADJUST_IGNORE_CLIFF_WALLS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"COMMANDO_BONUS_IGNORE_CLIFF_WALLS",
		"Ignore",
		1
	);
	
```

