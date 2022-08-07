---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_ROCK_BAND_UNIT_ALBUM_SALES
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_ROCK_BAND_UNIT_ALBUM_SALES
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="NOBEL_PRIZE_LIT_FIRST_PLACE_ROCK_BAND_BUFF"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"NOBEL_PRIZE_LIT_FIRST_PLACE_ROCK_BAND_BUFF",
		"MODIFIER_EMERGENCY_PLAYERS_ADJUST_ROCK_BAND_UNIT_ALBUM_SALES",
		"SCORED_COMPETITION_FIRST_PLACE_REQUIREMENTS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"NOBEL_PRIZE_LIT_FIRST_PLACE_ROCK_BAND_BUFF",
		"Amount",
		50
	);
	
```

