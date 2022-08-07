---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_RELIGIOUS_COMBAT_BONUS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_RELIGIOUS_COMBAT_BONUS
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="CARDINAL_GRAND_INQUISITOR_COMBAT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"CARDINAL_GRAND_INQUISITOR_COMBAT",
		"MODIFIER_SINGLE_CITY_RELIGIOUS_COMBAT_BONUS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"CARDINAL_GRAND_INQUISITOR_COMBAT",
		"Amount",
		10
	);
	
```

