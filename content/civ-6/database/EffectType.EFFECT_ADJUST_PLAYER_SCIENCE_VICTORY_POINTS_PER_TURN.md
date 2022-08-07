---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_SCIENCE_VICTORY_POINTS_PER_TURN
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_SCIENCE_VICTORY_POINTS_PER_TURN
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="ISS_FIRST_PLACE_SPACESHIP_SPEED"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"ISS_FIRST_PLACE_SPACESHIP_SPEED",
		"MODIFIER_PLAYER_ADJUST_SCIENCE_VICTORY_POINTS_PER_TURN",
		"ISS_SPACESHIP_SPEED_REQUIREMENTS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"ISS_FIRST_PLACE_SPACESHIP_SPEED",
		"Amount",
		3
	);
	
```

