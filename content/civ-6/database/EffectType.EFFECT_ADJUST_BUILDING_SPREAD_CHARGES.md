---
tags:
- EffectType
title: EFFECT_ADJUST_BUILDING_SPREAD_CHARGES
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_BUILDING_SPREAD_CHARGES
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="MOSQUE_ADJUST_SPREAD_CHARGES"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		Permanent,
		SubjectRequirementSetId
	)
VALUES
	(
		"MOSQUE_ADJUST_SPREAD_CHARGES",
		"MODIFIER_SINGLE_CITY_RELIGIOUS_SPREADS",
		1,
		"MOSQUE_RELIGIOUS_UNIT"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"MOSQUE_ADJUST_SPREAD_CHARGES",
		"Amount",
		1
	);
	
```

