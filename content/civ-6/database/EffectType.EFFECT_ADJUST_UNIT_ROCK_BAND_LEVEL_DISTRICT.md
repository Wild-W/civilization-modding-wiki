---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_ROCK_BAND_LEVEL_DISTRICT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_ROCK_BAND_LEVEL_DISTRICT
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Integer`
>	* DistrictType `String`

## Samples
```SQL {title="ROCKBAND_SPACE_ROCK_SEOWON"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"ROCKBAND_SPACE_ROCK_SEOWON",
		"MODIFIER_PLAYER_UNIT_ADJUST_ROCK_BAND_LEVEL_DISTRICT"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"ROCKBAND_SPACE_ROCK_SEOWON",
		"Amount",
		1
	),
	(
		"ROCKBAND_SPACE_ROCK_SEOWON",
		"DistrictType",
		"DISTRICT_SEOWON"
	);
	
```

