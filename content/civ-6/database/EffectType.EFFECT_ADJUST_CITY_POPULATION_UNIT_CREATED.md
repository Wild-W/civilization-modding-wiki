---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_POPULATION_UNIT_CREATED
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_POPULATION_UNIT_CREATED
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`
>	* UnitType `String`

## Samples
```SQL {title="JANISSARY_LOSE_POPULATION_IN_FOUNDED_CITIES"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"JANISSARY_LOSE_POPULATION_IN_FOUNDED_CITIES",
		"MODIFIER_PLAYER_CITIES_CHANGE_POPULATION_CREATE_UNIT",
		"JANISSARY_CITY_FOUNDED"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"JANISSARY_LOSE_POPULATION_IN_FOUNDED_CITIES",
		"Amount",
		"-1"
	),
	(
		"JANISSARY_LOSE_POPULATION_IN_FOUNDED_CITIES",
		"UnitType",
		"UNIT_SULEIMAN_JANISSARY"
	);
	
```

