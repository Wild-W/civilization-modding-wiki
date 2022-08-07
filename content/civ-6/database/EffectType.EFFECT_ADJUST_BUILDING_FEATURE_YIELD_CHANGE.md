---
tags:
- EffectType
title: EFFECT_ADJUST_BUILDING_FEATURE_YIELD_CHANGE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_BUILDING_FEATURE_YIELD_CHANGE
>
> * Class: `Unknown`
> * Parameters:
>	* Amount `Unknown`
>	* FeatureType `Unknown`
>	* YieldType `Unknown`

## Samples
```SQL {title="TRAIT_FOREST_BUILDINGS_CULTURE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_FOREST_BUILDINGS_CULTURE",
		"MODIFIER_PLAYER_CITIES_ADJUST_BUILDING_FEATURE_YIELD_CHANGE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_FOREST_BUILDINGS_CULTURE",
		"Amount",
		1
	),
	(
		"TRAIT_FOREST_BUILDINGS_CULTURE",
		"FeatureType",
		"FEATURE_FOREST"
	),
	(
		"TRAIT_FOREST_BUILDINGS_CULTURE",
		"YieldType",
		"YIELD_CULTURE"
	);
	
```

