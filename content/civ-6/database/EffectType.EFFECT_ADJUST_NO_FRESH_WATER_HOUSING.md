---
tags:
- EffectType
title: EFFECT_ADJUST_NO_FRESH_WATER_HOUSING
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_NO_FRESH_WATER_HOUSING
>
> * Class: `CITIES`
> * Parameters:
>	* NoHousing `Boolean`

## Samples
```SQL {title="TRAIT_NO_FRESH_WATER_HOUSING"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_NO_FRESH_WATER_HOUSING",
		"MODIFIER_PLAYER_CITIES_ADJUST_NO_FRESH_WATER_HOUSING"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_NO_FRESH_WATER_HOUSING",
		"NoHousing",
		1
	);
	
```

