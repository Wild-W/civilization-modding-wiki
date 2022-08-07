---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_COMBAT_BONUS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_COMBAT_BONUS
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="GARRISON_COMMANDER_ADJUST_CITY_COMBAT_BONUS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"GARRISON_COMMANDER_ADJUST_CITY_COMBAT_BONUS",
		"MODIFIER_CITY_ADJUST_CITY_COMBAT_BONUS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"GARRISON_COMMANDER_ADJUST_CITY_COMBAT_BONUS",
		"Amount",
		5
	);
	
```

