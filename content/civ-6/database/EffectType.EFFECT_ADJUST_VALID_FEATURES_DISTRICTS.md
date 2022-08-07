---
tags:
- EffectType
title: EFFECT_ADJUST_VALID_FEATURES_DISTRICTS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_VALID_FEATURES_DISTRICTS
>
> * Class: `CITIES`
> * Parameters:
>	* DistrictType `String`
>		* [Districts.DistrictType]
>	* FeatureType `String`
>		* [Features.FeatureType]

## Samples
```SQL {title="TRAIT_FLOODPLAINS_VALID_GOVERNMENT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_FLOODPLAINS_VALID_GOVERNMENT",
		"MODIFIER_PLAYER_CITIES_ADJUST_VALID_FEATURES_DISTRICTS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_FLOODPLAINS_VALID_GOVERNMENT",
		"DistrictType",
		"DISTRICT_GOVERNMENT"
	),
	(
		"TRAIT_FLOODPLAINS_VALID_GOVERNMENT",
		"FeatureType",
		"FEATURE_FLOODPLAINS"
	);
	
```

