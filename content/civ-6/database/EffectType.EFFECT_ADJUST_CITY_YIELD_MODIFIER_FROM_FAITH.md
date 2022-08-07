---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_YIELD_MODIFIER_FROM_FAITH
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_YIELD_MODIFIER_FROM_FAITH
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples
```SQL {title="TRAIT_FAITH_INTO_SCIENCE_HILLS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"TRAIT_FAITH_INTO_SCIENCE_HILLS",
		"MODIFIER_PLAYER_CITIES_ADJUST_YIELD_MODIFIER_FROM_FAITH",
		"ETHIOPIA_PLOT_IS_HILLS_REQUIREMENTS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_FAITH_INTO_SCIENCE_HILLS",
		"Amount",
		15
	),
	(
		"TRAIT_FAITH_INTO_SCIENCE_HILLS",
		"YieldType",
		"YIELD_SCIENCE"
	);
	
```

