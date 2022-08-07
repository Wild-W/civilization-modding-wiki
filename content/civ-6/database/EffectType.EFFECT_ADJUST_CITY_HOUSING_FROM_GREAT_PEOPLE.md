---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_HOUSING_FROM_GREAT_PEOPLE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_HOUSING_FROM_GREAT_PEOPLE
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="GREATPERSON_CITY_HOUSING_SMALL"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent
	)
VALUES
	(
		"GREATPERSON_CITY_HOUSING_SMALL",
		"MODIFIER_SINGLE_CITY_ADJUST_CITY_HOUSING_FROM_GREAT_PEOPLE",
		1,
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
		"GREATPERSON_CITY_HOUSING_SMALL",
		"Amount",
		1
	);
	
```

