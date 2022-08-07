---
tags:
- EffectType
title: EFFECT_ADJUST_FEATURE_PREREQ
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_FEATURE_PREREQ
>
> * Class: `Unknown`
> * Parameters:
>	* CivicType `Unknown`
>	* FeatureType `Unknown`

## Samples
```SQL {title="TRAIT_PLANT_MEDIEVAL_WOODS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_PLANT_MEDIEVAL_WOODS",
		"MODIFIER_PLAYER_ADJUST_FEATURE_UNLOCK"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_PLANT_MEDIEVAL_WOODS",
		"CivicType",
		"CIVIC_MEDIEVAL_FAIRES"
	),
	(
		"TRAIT_PLANT_MEDIEVAL_WOODS",
		"FeatureType",
		"FEATURE_FOREST"
	);
	
```

