---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_REQUIRED_POWER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_REQUIRED_POWER
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="PROJECT_COMPLETION_TERRESTRIAL_LASER_REQUIRED_POWER"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"PROJECT_COMPLETION_TERRESTRIAL_LASER_REQUIRED_POWER",
		"MODIFIER_SINGLE_CITY_ADJUST_REQUIRED_POWER"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"PROJECT_COMPLETION_TERRESTRIAL_LASER_REQUIRED_POWER",
		"Amount",
		5
	);
	
```

