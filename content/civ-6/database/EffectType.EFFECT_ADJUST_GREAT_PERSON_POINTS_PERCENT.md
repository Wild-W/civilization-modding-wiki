---
tags:
- EffectType
title: EFFECT_ADJUST_GREAT_PERSON_POINTS_PERCENT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_GREAT_PERSON_POINTS_PERCENT
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`
>	* GreatPersonClassType `String`
>		* [GreatPersonClasses.GreatPersonClassType]

## Samples
```SQL {title="TRAIT_DOUBLE_WRITER_POINTS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_DOUBLE_WRITER_POINTS",
		"MODIFIER_PLAYER_ADJUST_GREAT_PERSON_POINTS_PERCENT"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_DOUBLE_WRITER_POINTS",
		"Amount",
		50
	),
	(
		"TRAIT_DOUBLE_WRITER_POINTS",
		"GreatPersonClassType",
		"GREAT_PERSON_CLASS_WRITER"
	);
	
```

