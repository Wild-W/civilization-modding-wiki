---
tags:
- EffectType
title: EFFECT_ADJUST_GREAT_PEOPLE_POINTS_PER_KILL
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_GREAT_PEOPLE_POINTS_PER_KILL
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Integer`
>	* GreatPersonClassType `String`
>		* [GreatPersonClasses.GreatPersonClassType]

## Samples

```SQL {title="GARDE_GREAT_GENERAL_POINTS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"GARDE_GREAT_GENERAL_POINTS",
		"MODIFIER_PLAYER_UNIT_ADJUST_GREAT_PEOPLE_POINTS_PER_KILL"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"GARDE_GREAT_GENERAL_POINTS",
		"Amount",
		10
	),
	(
		"GARDE_GREAT_GENERAL_POINTS",
		"GreatPersonClassType",
		"GREAT_PERSON_CLASS_GENERAL"
	);
	
```

