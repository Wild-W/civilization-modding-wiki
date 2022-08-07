---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_AMENITIES_FROM_CITY_STATES
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_AMENITIES_FROM_CITY_STATES
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="MINOR_CIV_MUSCAT_COMMERCIAL_HUB_AMENITY_BONUS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"MINOR_CIV_MUSCAT_COMMERCIAL_HUB_AMENITY_BONUS",
		"MODIFIER_PLAYER_CITIES_ADJUST_CITY_AMENITIES_FROM_CITY_STATES",
		"CITY_HAS_COMMERCIAL_HUB_VIKING"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"MINOR_CIV_MUSCAT_COMMERCIAL_HUB_AMENITY_BONUS",
		"Amount",
		1
	);
	
```

