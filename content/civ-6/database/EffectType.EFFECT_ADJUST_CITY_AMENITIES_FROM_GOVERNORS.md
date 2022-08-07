---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_AMENITIES_FROM_GOVERNORS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_AMENITIES_FROM_GOVERNORS
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="GOV_TALL_AMENITY_BUFF"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"GOV_TALL_AMENITY_BUFF",
		"MODIFIER_PLAYER_CITIES_ADJUST_AMENITIES_FROM_GOVERNORS",
		"CITY_HAS_GOVERNOR_REQUIREMENTS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"GOV_TALL_AMENITY_BUFF",
		"Amount",
		2
	);
	
```

