---
tags:
- EffectType
title: EFFECT_ADJUST_GOLD_DISPERSAL
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_GOLD_DISPERSAL
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`
>	* Improvement `String`
>		* [Improvements.ImprovementType]

## Samples

```SQL {title="BARBARIAN_CAMP_GOLD_SCALING"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		OwnerRequirementSetId
	)
VALUES
	(
		"BARBARIAN_CAMP_GOLD_SCALING",
		"MODIFIER_PLAYER_ADJUST_GOLD_DISPERSAL",
		"PLAYER_IS_HUMAN"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Type,
		Value,
		Extra,
		SecondExtra
	)
VALUES
	(
		"BARBARIAN_CAMP_GOLD_SCALING",
		"Amount",
		"LinearScaleFromDefaultHandicap",
		0,
		"-5",
		"DIFFICULTY_PRINCE"
	),
	(
		"BARBARIAN_CAMP_GOLD_SCALING",
		"Improvement",
		"ARGTYPE_IDENTITY",
		"IMPROVEMENT_BARBARIAN_CAMP",
		NULL,
		NULL
	);
	
```

