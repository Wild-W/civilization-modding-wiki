---
tags:
- EffectType
title: EFFECT_ADJUST_ADD_AMENITY_PER_ADJACENT_LUXURY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_ADD_AMENITY_PER_ADJACENT_LUXURY
>
> * Class: `CITIES`
> * Parameters:
>	* AddAmenity `Boolean`

## Samples
```SQL {title="TRAIT_ADD_AMENITY_PER_ADJACENT_LUXURY"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_ADD_AMENITY_PER_ADJACENT_LUXURY",
		"MODIFIER_PLAYER_CITIES_ADD_AMENITY_PER_ADJACENT_LUXURY"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_ADD_AMENITY_PER_ADJACENT_LUXURY",
		"AddAmenity",
		1
	);
	
```

