---
tags:
- EffectType
title: EFFECT_ADJUST_RIVER_WONDER_PRODUCTION
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_RIVER_WONDER_PRODUCTION
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="TRAIT_RIVER_FASTER_BUILDTIME_WONDER"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_RIVER_FASTER_BUILDTIME_WONDER",
		"MODIFIER_PLAYER_CITIES_ADJUST_RIVER_WONDER_PRODUCTION"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_RIVER_FASTER_BUILDTIME_WONDER",
		"Amount",
		15
	);
	
```
