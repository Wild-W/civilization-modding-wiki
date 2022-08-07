---
tags:
- EffectType
title: EFFECT_ADJUST_GREAT_PEOPLE_POINTS_PER_KILL_BY_DEFEATED_STRENGTH
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_GREAT_PEOPLE_POINTS_PER_KILL_BY_DEFEATED_STRENGTH
>
> * Class: `Unknown`
> * Parameters:
>	* Amount `Unknown`
>	* GreatPersonClassType `Unknown`

## Samples

```SQL {title="WOLIN_GREAT_GENERAL_POINTS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"WOLIN_GREAT_GENERAL_POINTS",
		"MODIFIER_PLAYER_ADJUST_UNITS_GREAT_PEOPLE_POINTS_PER_KILL_BY_DEFEATED_STRENGTH"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"WOLIN_GREAT_GENERAL_POINTS",
		"Amount",
		25
	),
	(
		"WOLIN_GREAT_GENERAL_POINTS",
		"GreatPersonClassType",
		"GREAT_PERSON_CLASS_GENERAL"
	);
	
```

