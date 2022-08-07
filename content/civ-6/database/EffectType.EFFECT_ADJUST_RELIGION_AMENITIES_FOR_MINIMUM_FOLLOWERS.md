---
tags:
- EffectType
title: EFFECT_ADJUST_RELIGION_AMENITIES_FOR_MINIMUM_FOLLOWERS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_RELIGION_AMENITIES_FOR_MINIMUM_FOLLOWERS
>
> * Class: `CITIES`
> * Parameters:
>	* Amenities `Integer`
>	* Followers `Integer`

## Samples
```SQL {title="TRAIT_AMENITIES_FOR_MIN_FOLLOWERS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_AMENITIES_FOR_MIN_FOLLOWERS",
		"MODIFIER_PLAYER_CITIES_ADJUST_RELIGION_AMENITIES_FOR_MINIMUM_FOLLOWERS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_AMENITIES_FOR_MIN_FOLLOWERS",
		"Amenities",
		1
	),
	(
		"TRAIT_AMENITIES_FOR_MIN_FOLLOWERS",
		"Followers",
		1
	);
	
```

