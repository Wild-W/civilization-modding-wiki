---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_HAPPINESS_GREAT_PERSON
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_HAPPINESS_GREAT_PERSON
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`
>	* GreatPersonClassType `String`
>		* [GreatPersonClasses.GreatPersonClassType]
>	* HappinessType `String`
>		* [Happinesses.HappinessType]

## Samples
```SQL {title="TRAIT_SCIENTIST_HAPPY"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"TRAIT_SCIENTIST_HAPPY",
		"MODIFIER_PLAYER_CITIES_ADJUST_HAPPINESS_GREAT_PERSON",
		"PLAYER_HAS_CAMPUS_HAPPY_REQUIREMENTS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_SCIENTIST_HAPPY",
		"Amount",
		1
	),
	(
		"TRAIT_SCIENTIST_HAPPY",
		"GreatPersonClassType",
		"GREAT_PERSON_CLASS_SCIENTIST"
	),
	(
		"TRAIT_SCIENTIST_HAPPY",
		"HappinessType",
		"HAPPINESS_HAPPY"
	);
	
```

