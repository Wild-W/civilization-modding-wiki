---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_HAPPINESS_YIELD
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_HAPPINESS_YIELD
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`
>	* HappinessType `String`
>		* [Happinesses.HappinessType]
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples
```SQL {title="TRAIT_SCIENCE_HAPPY"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_SCIENCE_HAPPY",
		"MODIFIER_PLAYER_CITIES_ADJUST_HAPPINESS_YIELD"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_SCIENCE_HAPPY",
		"Amount",
		5
	),
	(
		"TRAIT_SCIENCE_HAPPY",
		"HappinessType",
		"HAPPINESS_HAPPY"
	),
	(
		"TRAIT_SCIENCE_HAPPY",
		"YieldType",
		"YIELD_SCIENCE"
	);
	
```

