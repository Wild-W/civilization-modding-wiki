---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_EXTRA_ACCUMULATION
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_EXTRA_ACCUMULATION
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="DEFENSE_LOGISTICS_BONUS_STRATEGICS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"DEFENSE_LOGISTICS_BONUS_STRATEGICS",
		"MODIFIER_SINGLE_CITY_ADJUST_EXTRA_ACCUMULATION"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"DEFENSE_LOGISTICS_BONUS_STRATEGICS",
		"Amount",
		1
	);
	
```

