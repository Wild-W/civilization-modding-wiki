---
tags:
- EffectType
title: EFFECT_TERRAIN_ADJACENCY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_TERRAIN_ADJACENCY
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`
>	* Description `String`
>	* DistrictType `String`
>		* [Districts.DistrictType]
>	* TerrainType `String`
>		* [Terrains.TerrainType]
>	* TilesRequired `Integer`
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples
```SQL {title="DANCE_OF_THE_AURORA_FAITHTUNDRAADJACENCY"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"DANCE_OF_THE_AURORA_FAITHTUNDRAADJACENCY",
		"MODIFIER_ALL_CITIES_TERRAIN_ADJACENCY",
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
		"DANCE_OF_THE_AURORA_FAITHTUNDRAADJACENCY",
		"Amount",
		1
	),
	(
		"DANCE_OF_THE_AURORA_FAITHTUNDRAADJACENCY",
		"Description",
		"LOC_DISTRICT_TUNDRA_FAITH"
	),
	(
		"DANCE_OF_THE_AURORA_FAITHTUNDRAADJACENCY",
		"DistrictType",
		"DISTRICT_HOLY_SITE"
	),
	(
		"DANCE_OF_THE_AURORA_FAITHTUNDRAADJACENCY",
		"TerrainType",
		"TERRAIN_TUNDRA"
	),
	(
		"DANCE_OF_THE_AURORA_FAITHTUNDRAADJACENCY",
		"YieldType",
		"YIELD_FAITH"
	);
	
```

```SQL {title="TRAIT_NUSANTARA_COAST_HOLY_SITE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_NUSANTARA_COAST_HOLY_SITE",
		"MODIFIER_PLAYER_CITIES_TERRAIN_ADJACENCY"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_NUSANTARA_COAST_HOLY_SITE",
		"Amount",
		1
	),
	(
		"TRAIT_NUSANTARA_COAST_HOLY_SITE",
		"Description",
		"LOC_DISTRICT_NUSANTARA_FAITH"
	),
	(
		"TRAIT_NUSANTARA_COAST_HOLY_SITE",
		"DistrictType",
		"DISTRICT_HOLY_SITE"
	),
	(
		"TRAIT_NUSANTARA_COAST_HOLY_SITE",
		"TerrainType",
		"TERRAIN_COAST"
	),
	(
		"TRAIT_NUSANTARA_COAST_HOLY_SITE",
		"TilesRequired",
		2
	),
	(
		"TRAIT_NUSANTARA_COAST_HOLY_SITE",
		"YieldType",
		"YIELD_FAITH"
	);
	
```

