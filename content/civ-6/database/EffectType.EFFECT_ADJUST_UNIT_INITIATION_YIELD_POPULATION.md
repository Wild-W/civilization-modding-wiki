---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_INITIATION_YIELD_POPULATION
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_INITIATION_YIELD_POPULATION
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Integer`
>	* YieldType `String`

## Samples

```SQL {title="MINOR_CIV_FEZ_INITIATION_SCIENCE_POPULATION"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"MINOR_CIV_FEZ_INITIATION_SCIENCE_POPULATION",
		"MODIFIER_PLAYER_UNITS_ADJUST_INITIATION_YIELD_POPULATION"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"MINOR_CIV_FEZ_INITIATION_SCIENCE_POPULATION",
		"Amount",
		20
	),
	(
		"MINOR_CIV_FEZ_INITIATION_SCIENCE_POPULATION",
		"YieldType",
		"YIELD_SCIENCE"
	);
	
```

