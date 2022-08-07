---
tags:
- EffectType
title: EFFECT_ADJUST_DISTRICT_YIELD_CHANGE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_DISTRICT_YIELD_CHANGE
>
> * Class: `DISTRICTS`
> * Parameters:
>	* Amount `Integer`
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples
```SQL {title="MINOR_CIV_SCIENTIFIC_YIELD_FOR_CAMPUS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"MINOR_CIV_SCIENTIFIC_YIELD_FOR_CAMPUS",
		"MODIFIER_PLAYER_DISTRICTS_ADJUST_YIELD_CHANGE",
		"DISTRICT_IS_CAMPUS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"MINOR_CIV_SCIENTIFIC_YIELD_FOR_CAMPUS",
		"Amount",
		2
	),
	(
		"MINOR_CIV_SCIENTIFIC_YIELD_FOR_CAMPUS",
		"YieldType",
		"YIELD_SCIENCE"
	);
	
```

