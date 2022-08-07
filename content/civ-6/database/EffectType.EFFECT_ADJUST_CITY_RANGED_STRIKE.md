---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_RANGED_STRIKE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_RANGED_STRIKE
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="BASTIONS_RANGEDSTRIKE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"BASTIONS_RANGEDSTRIKE",
		"MODIFIER_PLAYER_CITIES_ADJUST_RANGED_STRIKE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"BASTIONS_RANGEDSTRIKE",
		"Amount",
		5
	);
	
```

