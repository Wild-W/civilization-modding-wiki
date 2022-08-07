---
tags:
- EffectType
title: EFFECT_GRANT_PLAYER_RELIGIOUS_PRESSURE_GREAT_PERSON_ACTIVATED
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_GRANT_PLAYER_RELIGIOUS_PRESSURE_GREAT_PERSON_ACTIVATED
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="MINOR_CIV_VATICAN_CITY_GREAT_PERSON_RELIGIOUS_PRESSURE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"MINOR_CIV_VATICAN_CITY_GREAT_PERSON_RELIGIOUS_PRESSURE",
		"MODIFIER_PLAYER_GRANT_RELIGIOUS_PRESSURE_GREAT_PERSON_ACTIVATED"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"MINOR_CIV_VATICAN_CITY_GREAT_PERSON_RELIGIOUS_PRESSURE",
		"Amount",
		400
	);
	
```

