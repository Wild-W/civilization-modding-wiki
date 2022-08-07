---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_ENTERTAINMENT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_ENTERTAINMENT
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="THERMALBATH_ADDAMENITIES"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"THERMALBATH_ADDAMENITIES",
		"MODIFIER_SINGLE_CITY_ADJUST_ENTERTAINMENT",
		"CITY_HAS_1_OR_MORE_GEOTHERMALFISSURE_REQUIREMENTS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"THERMALBATH_ADDAMENITIES",
		"Amount",
		2
	);
	
```

