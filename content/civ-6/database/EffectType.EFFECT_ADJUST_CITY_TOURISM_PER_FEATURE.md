---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_TOURISM_PER_FEATURE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_TOURISM_PER_FEATURE
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="MARAE_TOURISM_FEATURES"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"MARAE_TOURISM_FEATURES",
		"MODIFIER_SINGLE_CITY_ADJUST_TOURISM_PER_FEATURE",
		"MAORI_MARAE_FLIGHT_REQUIREMENT"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"MARAE_TOURISM_FEATURES",
		"Amount",
		1
	);
	
```

