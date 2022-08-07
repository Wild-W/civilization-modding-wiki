---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_IMPROVEMENT_TOURISM
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_IMPROVEMENT_TOURISM
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="GOLDENGATE_IMPROVEMENT_TOURISM"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"GOLDENGATE_IMPROVEMENT_TOURISM",
		"MODIFIER_SINGLE_CITY_ADJUST_IMPROVEMENT_TOURISM"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"GOLDENGATE_IMPROVEMENT_TOURISM",
		"Amount",
		100
	);
	
```

