---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_TOURISM_BOMB_RANGE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_TOURISM_BOMB_RANGE
>
> * Class: `UNITS`
> * Parameters:
>	* Modifier `Integer`
>	* Range `Integer`

## Samples
```SQL {title="ROCKBAND_GOES_TO"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"ROCKBAND_GOES_TO",
		"MODIFIER_PLAYER_UNIT_ADJUST_TOURISM_BOMB_RANGE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"ROCKBAND_GOES_TO",
		"Modifier",
		"-50"
	),
	(
		"ROCKBAND_GOES_TO",
		"Range",
		10
	);
	
```

