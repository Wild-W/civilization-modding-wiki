---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_APPEAL
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_APPEAL
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="EIFFEL_TOWER_ADDAPPEAL"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"EIFFEL_TOWER_ADDAPPEAL",
		"MODIFIER_PLAYER_CITIES_ADJUST_CITY_APPEAL"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"EIFFEL_TOWER_ADDAPPEAL",
		"Amount",
		2
	);
	
```

