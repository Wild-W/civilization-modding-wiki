---
tags:
- EffectType
title: EFFECT_RIVER_ADJACENCY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_RIVER_ADJACENCY
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`
>	* Description `String`
>	* DistrictType `String`
>		* [Districts.DistrictType]
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples

```SQL {title="TRAIT_MONASTERIES_KING_HOLY_SITE_RIVER_ADJACENCY"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_MONASTERIES_KING_HOLY_SITE_RIVER_ADJACENCY",
		"MODIFIER_PLAYER_CITIES_RIVER_ADJACENCY"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_MONASTERIES_KING_HOLY_SITE_RIVER_ADJACENCY",
		"Amount",
		2
	),
	(
		"TRAIT_MONASTERIES_KING_HOLY_SITE_RIVER_ADJACENCY",
		"Description",
		"LOC_DISTRICT_RIVER_FAITH"
	),
	(
		"TRAIT_MONASTERIES_KING_HOLY_SITE_RIVER_ADJACENCY",
		"DistrictType",
		"DISTRICT_HOLY_SITE"
	),
	(
		"TRAIT_MONASTERIES_KING_HOLY_SITE_RIVER_ADJACENCY",
		"YieldType",
		"YIELD_FAITH"
	);
	
```

