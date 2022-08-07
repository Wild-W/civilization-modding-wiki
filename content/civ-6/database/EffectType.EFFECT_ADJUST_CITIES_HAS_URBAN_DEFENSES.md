---
tags:
- EffectType
title: EFFECT_ADJUST_CITIES_HAS_URBAN_DEFENSES
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITIES_HAS_URBAN_DEFENSES
>
> * Class: `CITIES`
> * Parameters:
>	* DefenseValue `Integer`

## Samples
```SQL {title="STEEL_UNLOCK_URBAN_DEFENSES"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"STEEL_UNLOCK_URBAN_DEFENSES",
		"MODIFIER_PLAYER_GRANT_CITIES_URBAN_DEFENSES"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"STEEL_UNLOCK_URBAN_DEFENSES",
		"DefenseValue",
		400
	);
	
```

