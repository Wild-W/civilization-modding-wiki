---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_RELIGION_EXTRA_PROMOTIONS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_RELIGION_EXTRA_PROMOTIONS
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="CARDINAL_PATRON_SAINT_PROMOTION"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"CARDINAL_PATRON_SAINT_PROMOTION",
		"MODIFIER_SINGLE_CITY_RELIGION_EXTRA_PROMOTIONS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"CARDINAL_PATRON_SAINT_PROMOTION",
		"Amount",
		1
	);
	
```

