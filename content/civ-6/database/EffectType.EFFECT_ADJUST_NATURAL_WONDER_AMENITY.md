---
tags:
- EffectType
title: EFFECT_ADJUST_NATURAL_WONDER_AMENITY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_NATURAL_WONDER_AMENITY
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="PAMUKKALE_AMENITY"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		OwnerRequirementSetId,
		SubjectRequirementSetId
	)
VALUES
	(
		"PAMUKKALE_AMENITY",
		"MODIFIER_ALL_CITIES_ADJUST_NATURAL_WONDER_AMENITY",
		"PAMUKKALE_REQUIREMENTS",
		"CITY_HAS_PAMUKKALE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"PAMUKKALE_AMENITY",
		"Amount",
		1
	);
	
```

