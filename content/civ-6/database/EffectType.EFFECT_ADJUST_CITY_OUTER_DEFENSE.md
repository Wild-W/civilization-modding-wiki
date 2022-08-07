---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_OUTER_DEFENSE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_OUTER_DEFENSE
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="BASTIONS_OUTERDEFENSE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"BASTIONS_OUTERDEFENSE",
		"MODIFIER_PLAYER_CITIES_ADJUST_OUTER_DEFENSE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"BASTIONS_OUTERDEFENSE",
		"Amount",
		6
	);
	
```

