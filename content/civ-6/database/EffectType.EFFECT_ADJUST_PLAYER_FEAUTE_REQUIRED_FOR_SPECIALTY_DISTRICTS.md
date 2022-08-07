---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_FEAUTE_REQUIRED_FOR_SPECIALTY_DISTRICTS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_FEAUTE_REQUIRED_FOR_SPECIALTY_DISTRICTS
>
> * Class: `PLAYERS`
> * Parameters:
>	* FeatureType `Unknown`

## Samples

```SQL {title="TRAIT_DISTRICTS_FOREST_ONLY"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_DISTRICTS_FOREST_ONLY",
		"MODIFIER_PLAYER_ADJUST_FEAUTE_REQUIRED_FOR_SPECIALTY_DISTRICTS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_DISTRICTS_FOREST_ONLY",
		"FeatureType",
		"FEATURE_FOREST"
	);
	
```

