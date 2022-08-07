---
tags:
- EffectType
title: EFFECT_ADJUST_IMPROVEMENT_HOUSING
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_IMPROVEMENT_HOUSING
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="STEPWELL_HOUSING_WITHTECH"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"STEPWELL_HOUSING_WITHTECH",
		"MODIFIER_SINGLE_CITY_ADJUST_IMPROVEMENT_HOUSING",
		"PLAYER_HAS_TECHNOLOGY_REQUIREMENTS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"STEPWELL_HOUSING_WITHTECH",
		"Amount",
		1
	);
	
```

