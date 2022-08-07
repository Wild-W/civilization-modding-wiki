---
tags:
- EffectType
title: EFFECT_GRANT_YIELD_PER_GREAT_WORK_IN_CITY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_GRANT_YIELD_PER_GREAT_WORK_IN_CITY
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`
>	* GreatWorkObjectType `String`
>		* [GreatWorkObjectTypes.GreatWorkObjectType]
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples
```SQL {title="GREATPERSON_ARTIFACT_SCIENCE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent
	)
VALUES
	(
		"GREATPERSON_ARTIFACT_SCIENCE",
		"MODIFIER_SINGLE_CITY_GRANT_YIELD_PER_GREAT_WORK",
		1,
		1
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Type,
		Value
	)
VALUES
	(
		"GREATPERSON_ARTIFACT_SCIENCE",
		"Amount",
		"ScaleByGameSpeed",
		350
	),
	(
		"GREATPERSON_ARTIFACT_SCIENCE",
		"GreatWorkObjectType",
		"ARGTYPE_IDENTITY",
		"GREATWORKOBJECT_ARTIFACT"
	),
	(
		"GREATPERSON_ARTIFACT_SCIENCE",
		"YieldType",
		"ARGTYPE_IDENTITY",
		"YIELD_SCIENCE"
	);
	
```

