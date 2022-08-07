---
tags:
- EffectType
title: EFFECT_GRANT_GREAT_PERSON_CLASS_IN_CITY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_GRANT_GREAT_PERSON_CLASS_IN_CITY
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`
>	* GreatPersonClassType `String`
>		* [GreatPersonClasses.GreatPersonClassType]

## Samples

```SQL {title="STONEHENGE_GRANT_PROPHET"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent,
		SubjectRequirementSetId
	)
VALUES
	(
		"STONEHENGE_GRANT_PROPHET",
		"MODIFIER_SINGLE_CITY_GRANT_GREAT_PERSON_CLASS_IN_CITY",
		1,
		1,
		"STONEHENGE_PROPHET_REQUIREMENTS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"STONEHENGE_GRANT_PROPHET",
		"Amount",
		1
	),
	(
		"STONEHENGE_GRANT_PROPHET",
		"GreatPersonClassType",
		"GREAT_PERSON_CLASS_PROPHET"
	);
	
```

