---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_INNER_DEFENSE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_INNER_DEFENSE
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="PALACE_ADJUST_GARRISON_STRENGTH"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"PALACE_ADJUST_GARRISON_STRENGTH",
		"MODIFIER_PLAYER_CITIES_ADJUST_INNER_DEFENSE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"PALACE_ADJUST_GARRISON_STRENGTH",
		"Amount",
		3
	);
	
```

