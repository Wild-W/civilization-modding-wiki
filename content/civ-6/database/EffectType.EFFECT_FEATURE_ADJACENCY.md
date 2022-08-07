---
tags:
- EffectType
title: EFFECT_FEATURE_ADJACENCY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_FEATURE_ADJACENCY
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`
>	* Description `String`
>	* DistrictType `String`
>		* [Districts.DistrictType]
>	* FeatureType `String`
>		* [Features.FeatureType]
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples

```SQL {title="SACRED_PATH_FAITHFEATUREADJACENCY"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"SACRED_PATH_FAITHFEATUREADJACENCY",
		"MODIFIER_ALL_CITIES_FEATURE_ADJACENCY",
		"CITY_FOLLOWS_PANTHEON_REQUIREMENTS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"SACRED_PATH_FAITHFEATUREADJACENCY",
		"Amount",
		1
	),
	(
		"SACRED_PATH_FAITHFEATUREADJACENCY",
		"Description",
		"LOC_DISTRICT_JUNGLE_FAITH"
	),
	(
		"SACRED_PATH_FAITHFEATUREADJACENCY",
		"DistrictType",
		"DISTRICT_HOLY_SITE"
	),
	(
		"SACRED_PATH_FAITHFEATUREADJACENCY",
		"FeatureType",
		"FEATURE_JUNGLE"
	),
	(
		"SACRED_PATH_FAITHFEATUREADJACENCY",
		"YieldType",
		"YIELD_FAITH"
	);
	
```

