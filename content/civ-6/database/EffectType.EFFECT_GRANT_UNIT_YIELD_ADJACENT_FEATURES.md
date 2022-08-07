---
tags:
- EffectType
title: EFFECT_GRANT_UNIT_YIELD_ADJACENT_FEATURES
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_GRANT_UNIT_YIELD_ADJACENT_FEATURES
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Integer`
>	* FeatureType `String`
>		* [Features.FeatureType]
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples

```SQL {title="GREATPERSON_ADJACENT_RAINFOREST_SCIENCE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent
	)
VALUES
	(
		"GREATPERSON_ADJACENT_RAINFOREST_SCIENCE",
		"MODIFIER_PLAYER_UNIT_GRANT_ADJACENT_FEATURE_YIELD",
		1,
		1
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Type,
		Value
	)
VALUES
	(
		"GREATPERSON_ADJACENT_RAINFOREST_SCIENCE",
		"Amount",
		"ScaleByGameSpeed",
		400
	),
	(
		"GREATPERSON_ADJACENT_RAINFOREST_SCIENCE",
		"FeatureType",
		"ARGTYPE_IDENTITY",
		"FEATURE_JUNGLE"
	),
	(
		"GREATPERSON_ADJACENT_RAINFOREST_SCIENCE",
		"YieldType",
		"ARGTYPE_IDENTITY",
		"YIELD_SCIENCE"
	);
	
```

