---
tags:
- EffectType
title: EFFECT_TREAT_CAPITAL_AS_HOLY_CITY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_TREAT_CAPITAL_AS_HOLY_CITY
>
> * Class: `PLAYERS`
> * Parameters:
>	* Value `Integer`

## Samples
```SQL {title="MINOR_CIV_JERUSALEM_HOLY_CITY_BONUS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"MINOR_CIV_JERUSALEM_HOLY_CITY_BONUS",
		"MODIFIER_PLAYER_TREAT_CAPITAL_AS_HOLY_CITY"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"MINOR_CIV_JERUSALEM_HOLY_CITY_BONUS",
		"Value",
		1
	);
	
```

