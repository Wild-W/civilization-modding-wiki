---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_POPULATION
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_POPULATION
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="GOODY_SURVIVORS_ADD_POPULATION"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent
	)
VALUES
	(
		"GOODY_SURVIVORS_ADD_POPULATION",
		"MODIFIER_PLAYER_NEAREST_CITY_ADD_POPULATION",
		1,
		1
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"GOODY_SURVIVORS_ADD_POPULATION",
		"Amount",
		1
	);
	
```

