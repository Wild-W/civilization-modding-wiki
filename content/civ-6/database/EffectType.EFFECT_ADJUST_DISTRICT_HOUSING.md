---
tags:
- EffectType
title: EFFECT_ADJUST_DISTRICT_HOUSING
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_DISTRICT_HOUSING
>
> * Class: `DISTRICTS`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="TRAIT_HOLY_SITE_RIVER_2HOUSING"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"TRAIT_HOLY_SITE_RIVER_2HOUSING",
		"MODIFIER_PLAYER_DISTRICTS_ADJUST_HOUSING",
		"PLOT_IS_HOLY_SITE_RIVER_HOUSING_REQUIREMENTS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_HOLY_SITE_RIVER_2HOUSING",
		"Amount",
		2
	);
	
```

