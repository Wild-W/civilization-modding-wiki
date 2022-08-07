---
tags:
- EffectType
title: EFFECT_ADJUST_ALL_DISTRICT_PRODUCTION_MODIFIER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_ALL_DISTRICT_PRODUCTION_MODIFIER
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="CITY_PATRON_GODDESS_DISTRICT_PRODUCTION_MODIFIER"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"CITY_PATRON_GODDESS_DISTRICT_PRODUCTION_MODIFIER",
		"MODIFIER_SINGLE_CITY_ADJUST_DISTRICT_PRODUCTION_MODIFIER",
		"CITY_HAS_0_SPECIALTY_DISTRICTS_REQUIREMENTS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"CITY_PATRON_GODDESS_DISTRICT_PRODUCTION_MODIFIER",
		"Amount",
		25
	);
	
```

