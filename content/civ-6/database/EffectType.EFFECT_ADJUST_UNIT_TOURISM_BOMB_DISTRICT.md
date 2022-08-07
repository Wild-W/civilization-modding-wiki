---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_TOURISM_BOMB_DISTRICT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_TOURISM_BOMB_DISTRICT
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Integer`
>	* DistrictType `String`
>		* [Districts.DistrictType]

## Samples
```SQL {title="ROCKBAND_SPACE_ROCK_SEOWON_MODIFIER"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"ROCKBAND_SPACE_ROCK_SEOWON_MODIFIER",
		"MODIFIER_PLAYER_UNIT_ADJUST_TOURISM_BOMB_DISTRICT"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"ROCKBAND_SPACE_ROCK_SEOWON_MODIFIER",
		"Amount",
		500
	),
	(
		"ROCKBAND_SPACE_ROCK_SEOWON_MODIFIER",
		"DistrictType",
		"DISTRICT_SEOWON"
	);
	
```

