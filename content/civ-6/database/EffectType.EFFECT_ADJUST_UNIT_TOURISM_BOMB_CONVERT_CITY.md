---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_TOURISM_BOMB_CONVERT_CITY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_TOURISM_BOMB_CONVERT_CITY
>
> * Class: `UNITS`
> * Parameters:
>	* Convert `Boolean`

## Samples
```SQL {title="ROCKBAND_RELIGIOUS_ROCK"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"ROCKBAND_RELIGIOUS_ROCK",
		"MODIFIER_PLAYER_UNIT_ADJUST_TOURISM_BOMB_CONVERT_CITY"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"ROCKBAND_RELIGIOUS_ROCK",
		"Convert",
		1
	);
	
```

