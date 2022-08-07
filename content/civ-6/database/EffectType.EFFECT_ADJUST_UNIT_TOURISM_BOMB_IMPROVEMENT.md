---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_TOURISM_BOMB_IMPROVEMENT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_TOURISM_BOMB_IMPROVEMENT
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Integer`
>	* ImprovementType `String`
>		* [Improvements.ImprovementType]

## Samples

```SQL {title="ROCKBAND_SURF_ROCK_TOURISM_BOMB"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"ROCKBAND_SURF_ROCK_TOURISM_BOMB",
		"MODIFIER_PLAYER_UNIT_ADJUST_TOURISM_BOMB_IMPROVEMENT"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"ROCKBAND_SURF_ROCK_TOURISM_BOMB",
		"Amount",
		500
	),
	(
		"ROCKBAND_SURF_ROCK_TOURISM_BOMB",
		"ImprovementType",
		"IMPROVEMENT_BEACH_RESORT"
	);
	
```

