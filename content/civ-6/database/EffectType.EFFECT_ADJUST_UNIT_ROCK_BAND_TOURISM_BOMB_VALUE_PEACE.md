---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_ROCK_BAND_TOURISM_BOMB_VALUE_PEACE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_ROCK_BAND_TOURISM_BOMB_VALUE_PEACE
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="FLOWER_POWER_TOURISM_BOMB_CONCERT_VALUE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"FLOWER_POWER_TOURISM_BOMB_CONCERT_VALUE",
		"MODIFIER_PLAYER_UNITS_ADJUST_ROCK_BAND_TOURISM_BOMB_VALUE_PEACE",
		"UNIT_IS_ROCK_BAND"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"FLOWER_POWER_TOURISM_BOMB_CONCERT_VALUE",
		"Amount",
		50
	);
	
```

