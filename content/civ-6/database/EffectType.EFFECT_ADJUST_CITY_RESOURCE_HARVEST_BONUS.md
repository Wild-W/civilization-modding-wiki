---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_RESOURCE_HARVEST_BONUS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_RESOURCE_HARVEST_BONUS
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="GROUNDBREAKER_BONUS_HARVEST_YIELDS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"GROUNDBREAKER_BONUS_HARVEST_YIELDS",
		"MODIFIER_CITY_ADJUST_RESOURCE_HARVEST_BONUS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"GROUNDBREAKER_BONUS_HARVEST_YIELDS",
		"Amount",
		50
	);
	
```

