---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_GROWTH
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_GROWTH
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="FERTILITY_RITES_GROWTH"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"FERTILITY_RITES_GROWTH",
		"MODIFIER_ALL_CITIES_ADJUST_CITY_GROWTH",
		"CITY_FOLLOWS_PANTHEON_REQUIREMENTS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"FERTILITY_RITES_GROWTH",
		"Amount",
		10
	);
	
```

