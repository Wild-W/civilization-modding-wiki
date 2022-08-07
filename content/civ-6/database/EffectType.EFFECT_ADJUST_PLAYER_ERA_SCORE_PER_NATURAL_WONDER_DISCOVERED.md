---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_ERA_SCORE_PER_NATURAL_WONDER_DISCOVERED
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_ERA_SCORE_PER_NATURAL_WONDER_DISCOVERED
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="COMMEMORATION_EXPLORATION_NATURAL_WONDER_QUEST"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"COMMEMORATION_EXPLORATION_NATURAL_WONDER_QUEST",
		"MODIFIER_PLAYER_ADJUST_PLAYER_ERA_SCORE_PER_NATURAL_WONDER_DISCOVERED",
		"PLAYER_ELIGIBLE_FOR_COMMEMORATION_QUEST"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"COMMEMORATION_EXPLORATION_NATURAL_WONDER_QUEST",
		"Amount",
		3
	);
	
```

