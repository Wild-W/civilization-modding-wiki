---
tags:
- EffectType
title: EFFECT_ADJUST_GREAT_PERSON_POINTS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_GREAT_PERSON_POINTS
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`
>	* GreatPersonClassType `String`
>		* [GreatPersonClasses.GreatPersonClassType]

## Samples

```SQL {title="TRAIT_SHRINE_WRITING_POINTS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"TRAIT_SHRINE_WRITING_POINTS",
		"MODIFIER_PLAYER_CITIES_ADJUST_GREAT_PERSON_POINT_BASE",
		"REQUIREMENTS_CITY_HAS_SHRINE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_SHRINE_WRITING_POINTS",
		"Amount",
		1
	),
	(
		"TRAIT_SHRINE_WRITING_POINTS",
		"GreatPersonClassType",
		"GREAT_PERSON_CLASS_WRITER"
	);
	
```

