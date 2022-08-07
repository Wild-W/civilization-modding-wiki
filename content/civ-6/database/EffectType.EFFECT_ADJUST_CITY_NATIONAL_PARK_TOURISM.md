---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_NATIONAL_PARK_TOURISM
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_NATIONAL_PARK_TOURISM
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="GOLDENGATE_NATIONAL_PARK_TOURISM"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"GOLDENGATE_NATIONAL_PARK_TOURISM",
		"MODIFIER_SINGLE_CITY_ADJUST_NATIONAL_PARK_TOURISM"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"GOLDENGATE_NATIONAL_PARK_TOURISM",
		"Amount",
		100
	);
	
```

