---
tags:
- EffectType
title: EFFECT_ADJUST_PLOT_YIELD
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLOT_YIELD
>
> * Class: `PLOTS`
> * Parameters:
>	* Amount `Integer`
>		* The amount of yield change.  Must be either a single value or multiple to match each yield type.
>	* ImprovementType `Unknown`
>	* ScalingFactor `Unknown`
>	* YieldType `String`
>		* One or more yield types separated by a comma.
>		* [Yields.YieldType]

## Samples
```SQL {title="LADY_OF_THE_REEDS_PRODUCTION_MODIFIER"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"LADY_OF_THE_REEDS_PRODUCTION_MODIFIER",
		"MODIFIER_CITY_PLOT_YIELDS_ADJUST_PLOT_YIELD",
		"PLOT_HAS_REEDS_REQUIREMENTS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"LADY_OF_THE_REEDS_PRODUCTION_MODIFIER",
		"Amount",
		1
	),
	(
		"LADY_OF_THE_REEDS_PRODUCTION_MODIFIER",
		"YieldType",
		"YIELD_PRODUCTION"
	);
	
```

```SQL {title="GAUL_MINE_TOURISM"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"GAUL_MINE_TOURISM",
		"MODIFIER_PLAYER_ADJUST_PLOT_YIELD",
		"PLAYER_HAS_FLIGHT"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"GAUL_MINE_TOURISM",
		"ImprovementType",
		"IMPROVEMENT_MINE"
	),
	(
		"GAUL_MINE_TOURISM",
		"ScalingFactor",
		200
	);
	
```

