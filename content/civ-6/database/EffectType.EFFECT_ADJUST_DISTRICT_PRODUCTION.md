---
tags:
- EffectType
title: EFFECT_ADJUST_DISTRICT_PRODUCTION
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_DISTRICT_PRODUCTION
>
> * Class: `DISTRICTS`
> * Parameters:
>	* Amount `Integer`
>	* DistrictType `String`
>		* [Districts.DistrictType]

## Samples
```SQL {title="TRAIT_BOOST_ENCAMPMENT_PRODUCTION"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_BOOST_ENCAMPMENT_PRODUCTION",
		"MODIFIER_PLAYER_CITIES_ADJUST_DISTRICT_PRODUCTION"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_BOOST_ENCAMPMENT_PRODUCTION",
		"Amount",
		100
	),
	(
		"TRAIT_BOOST_ENCAMPMENT_PRODUCTION",
		"DistrictType",
		"DISTRICT_ENCAMPMENT"
	);
	
```

