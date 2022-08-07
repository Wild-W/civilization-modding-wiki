---
tags:
- EffectType
title: EFFECT_ADJUST_FEATURE_APPEAL_MODIFIER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_FEATURE_APPEAL_MODIFIER
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`
>	* FeatureType `String`
>		* [Features.FeatureType]

## Samples
```SQL {title="TRAIT_AMAZON_RAINFOREST_EXTRA_APPEAL"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_AMAZON_RAINFOREST_EXTRA_APPEAL",
		"MODIFIER_PLAYER_CITIES_ADJUST_FEATURE_APPEAL_MODIFIER"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_AMAZON_RAINFOREST_EXTRA_APPEAL",
		"Amount",
		2
	),
	(
		"TRAIT_AMAZON_RAINFOREST_EXTRA_APPEAL",
		"FeatureType",
		"FEATURE_JUNGLE"
	);
	
```

