---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_ATTACKS_PER_TURN
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_ATTACKS_PER_TURN
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="CITY_DEFENDER_ADJUST_ATTACKS_PER_TURN"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"CITY_DEFENDER_ADJUST_ATTACKS_PER_TURN",
		"MODIFIER_CITY_ADJUST_ATTACKS_PER_TURN"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"CITY_DEFENDER_ADJUST_ATTACKS_PER_TURN",
		"Amount",
		1
	);
	
```

