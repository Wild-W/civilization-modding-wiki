---
tags:
- EffectType
title: EFFECT_ADJUST_WATER_HOUSING
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_WATER_HOUSING
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="TRAIT_COASTAL_HOUSING"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"TRAIT_COASTAL_HOUSING",
		"MODIFIER_PLAYER_CITIES_ADJUST_WATER_HOUSING",
		"PLOT_IS_COASTAL_LAND_REQUIREMENTS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_COASTAL_HOUSING",
		"Amount",
		3
	);
	
```

