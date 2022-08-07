---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_ALWAYS_LOYAL
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_ALWAYS_LOYAL
>
> * Class: `CITIES`
> * Parameters:
>	* AlwaysLoyal `Boolean`

## Samples
```SQL {title="STATUELIBERTY_CITIES_ALWAYS_LOYAL"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"STATUELIBERTY_CITIES_ALWAYS_LOYAL",
		"MODIFIER_PLAYER_CITIES_ADJUST_ALWAYS_LOYAL",
		"STATUELIBERTY_REQUIREMENTS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"STATUELIBERTY_CITIES_ALWAYS_LOYAL",
		"AlwaysLoyal",
		1
	);
	
```

