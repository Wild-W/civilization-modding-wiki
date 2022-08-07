---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_RELIGION_PRESSURE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_RELIGION_PRESSURE
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="CARDINAL_BISHOP_PRESSURE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"CARDINAL_BISHOP_PRESSURE",
		"MODIFIER_SINGLE_CITY_RELIGION_PRESSURE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"CARDINAL_BISHOP_PRESSURE",
		"Amount",
		100
	);
	
```

