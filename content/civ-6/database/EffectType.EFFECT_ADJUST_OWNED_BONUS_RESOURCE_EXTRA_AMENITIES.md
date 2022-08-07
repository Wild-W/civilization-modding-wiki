---
tags:
- EffectType
title: EFFECT_ADJUST_OWNED_BONUS_RESOURCE_EXTRA_AMENITIES
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_OWNED_BONUS_RESOURCE_EXTRA_AMENITIES
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="MINOR_CIV_BUENOS_AIRES_BONUS_RESOURCE_AMENITY_BONUS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"MINOR_CIV_BUENOS_AIRES_BONUS_RESOURCE_AMENITY_BONUS",
		"MODIFIER_PLAYER_OWNED_BONUS_RESOURCE_EXTRA_AMENITIES"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"MINOR_CIV_BUENOS_AIRES_BONUS_RESOURCE_AMENITY_BONUS",
		"Amount",
		1
	);
	
```

