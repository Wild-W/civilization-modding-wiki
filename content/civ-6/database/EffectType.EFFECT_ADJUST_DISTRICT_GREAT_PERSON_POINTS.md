---
tags:
- EffectType
title: EFFECT_ADJUST_DISTRICT_GREAT_PERSON_POINTS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_DISTRICT_GREAT_PERSON_POINTS
>
> * Class: `DISTRICTS`
> * Parameters:
>	* Amount `Integer`
>	* GreatPersonClassType `String`
>		* [GreatPersonClasses.GreatPersonClassType]

## Samples
```SQL {title="DIVINE_SPARK_HOLY_SITE_MODIFIER"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"DIVINE_SPARK_HOLY_SITE_MODIFIER",
		"MODIFIER_SINGLE_CITY_DISTRICTS_ADJUST_GREAT_PERSON_POINTS",
		"DISTRICT_IS_HOLY_SITE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"DIVINE_SPARK_HOLY_SITE_MODIFIER",
		"Amount",
		1
	),
	(
		"DIVINE_SPARK_HOLY_SITE_MODIFIER",
		"GreatPersonClassType",
		"GREAT_PERSON_CLASS_PROPHET"
	);
	
```

