---
tags:
- EffectType
title: EFFECT_ADJUST_ADJACENT_CITY_RIVER_BUILDING_PRODUCTION
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_ADJACENT_CITY_RIVER_BUILDING_PRODUCTION
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="TRAIT_CITY_ADJACENT_RIVER_BUILDING_PRODUCTION"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_CITY_ADJACENT_RIVER_BUILDING_PRODUCTION",
		"MODIFIER_PLAYER_CITIES_ADJUST_ADJACENT_RIVER_BUILDING_PRODUCTION"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_CITY_ADJACENT_RIVER_BUILDING_PRODUCTION",
		"Amount",
		50
	);
	
```

