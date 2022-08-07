---
tags:
- EffectType
title: EFFECT_ADJUST_IMPROVEMENT_AMENITY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_IMPROVEMENT_AMENITY
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="TEMPLE_ARTEMIS_CAMP_AMENITY"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"TEMPLE_ARTEMIS_CAMP_AMENITY",
		"MODIFIER_SINGLE_CITY_ADJUST_IMPROVEMENT_AMENITY",
		"TEMPLE_ARTEMIS_REQUIREMENTS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TEMPLE_ARTEMIS_CAMP_AMENITY",
		"Amount",
		1
	);
	
```

