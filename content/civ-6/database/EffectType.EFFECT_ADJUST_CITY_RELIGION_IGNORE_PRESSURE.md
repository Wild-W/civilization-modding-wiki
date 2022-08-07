---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_RELIGION_IGNORE_PRESSURE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_RELIGION_IGNORE_PRESSURE
>
> * Class: `CITIES`
> * Parameters:
>	* Enable `Boolean`

## Samples

```SQL {title="CARDINAL_CITADEL_OF_GOD_PRESSURE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"CARDINAL_CITADEL_OF_GOD_PRESSURE",
		"MODIFIER_SINGLE_CITY_RELIGION_IGNORE_PRESSURE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"CARDINAL_CITADEL_OF_GOD_PRESSURE",
		"Enable",
		1
	);
	
```

