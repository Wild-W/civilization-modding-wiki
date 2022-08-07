---
tags:
- EffectType
title: EFFECT_ADJUST_DISTRICT_YIELD_BASED_ON_APPEAL
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_DISTRICT_YIELD_BASED_ON_APPEAL
>
> * Class: `CITIES`
> * Parameters:
>	* Description `String`
>	* DistrictType `String`
>		* [Districts.DistrictType]
>	* RequiredAppeal `Integer`
>	* YieldChange `Integer`
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples
```SQL {title="TRAIT_CHARMING_CAMPUS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_CHARMING_CAMPUS",
		"MODIFIER_PLAYER_DISTRICTS_ADJUST_YIELD_BASED_ON_APPEAL"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_CHARMING_CAMPUS",
		"Description",
		"LOC_DISTRICT_APPEAL_SCIENCE"
	),
	(
		"TRAIT_CHARMING_CAMPUS",
		"DistrictType",
		"DISTRICT_CAMPUS"
	),
	(
		"TRAIT_CHARMING_CAMPUS",
		"RequiredAppeal",
		2
	),
	(
		"TRAIT_CHARMING_CAMPUS",
		"YieldChange",
		1
	),
	(
		"TRAIT_CHARMING_CAMPUS",
		"YieldType",
		"YIELD_SCIENCE"
	);
	
```

