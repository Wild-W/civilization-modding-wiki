---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_SPY_OFFENSIVE_OPERATION_TIME
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_SPY_OFFENSIVE_OPERATION_TIME
>
> * Class: `UNITS`
> * Parameters:
>	* ReductionPercent `Integer`

## Samples
```SQL {title="COMMEMORATION_ESPIONAGE_GA_REDUCTION"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		OwnerRequirementSetId,
		SubjectStackLimit
	)
VALUES
	(
		"COMMEMORATION_ESPIONAGE_GA_REDUCTION",
		"MODIFIER_PLAYER_UNITS_ADJUST_SPY_OFFENSIVE_OPERATION_TIME",
		"PLAYER_HAS_GOLDEN_AGE",
		1
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"COMMEMORATION_ESPIONAGE_GA_REDUCTION",
		"ReductionPercent",
		25
	);
	
```

