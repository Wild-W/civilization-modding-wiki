---
tags:
- EffectType
title: EFFECT_GRANT_PLAYER_SPECIFIC_TECH_BOOST_GREAT_PERSON
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_GRANT_PLAYER_SPECIFIC_TECH_BOOST_GREAT_PERSON
>
> * Class: `PLAYERS`
> * Parameters:
>	* GrantTechIfBoosted `Unknown`
>	* TechType `String`
>		* [Technologies.TechnologyType]

## Samples
```SQL {title="GREAT_PERSON_INDIVIDUAL_BOOST_OR_GRANT_MATHEMATICS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent
	)
VALUES
	(
		"GREAT_PERSON_INDIVIDUAL_BOOST_OR_GRANT_MATHEMATICS",
		"MODIFIER_PLAYER_GRANT_SPECIFIC_TECH_BOOST",
		1,
		1
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"GREAT_PERSON_INDIVIDUAL_BOOST_OR_GRANT_MATHEMATICS",
		"GrantTechIfBoosted",
		1
	),
	(
		"GREAT_PERSON_INDIVIDUAL_BOOST_OR_GRANT_MATHEMATICS",
		"TechType",
		"TECH_MATHEMATICS"
	);
	
```

```SQL {title="GREATPERSON_COMPUTERSTECHBOOST"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent
	)
VALUES
	(
		"GREATPERSON_COMPUTERSTECHBOOST",
		"MODIFIER_PLAYER_GRANT_SPECIFIC_TECH_BOOST",
		1,
		1
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"GREATPERSON_COMPUTERSTECHBOOST",
		"TechType",
		"TECH_COMPUTERS"
	);
	
```

