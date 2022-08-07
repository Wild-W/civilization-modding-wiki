---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_ROCK_BAND_LEVEL_IMPROVEMENT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_ROCK_BAND_LEVEL_IMPROVEMENT
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Integer`
>	* ImprovementType `String`

## Samples

```SQL {title="ROCKBAND_SURF_ROCK_LEVEL"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"ROCKBAND_SURF_ROCK_LEVEL",
		"MODIFIER_PLAYER_UNIT_ADJUST_ROCK_BAND_LEVEL_IMPROVEMENT"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"ROCKBAND_SURF_ROCK_LEVEL",
		"Amount",
		1
	),
	(
		"ROCKBAND_SURF_ROCK_LEVEL",
		"ImprovementType",
		"IMPROVEMENT_BEACH_RESORT"
	);
	
```

