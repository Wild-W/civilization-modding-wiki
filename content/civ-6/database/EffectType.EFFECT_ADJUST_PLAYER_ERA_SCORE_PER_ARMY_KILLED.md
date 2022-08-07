---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_ERA_SCORE_PER_ARMY_KILLED
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_ERA_SCORE_PER_ARMY_KILLED
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="COMMEMORATION_MILITARY_QUEST_ARMY"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"COMMEMORATION_MILITARY_QUEST_ARMY",
		"MODIFIER_PLAYER_ADJUST_PLAYER_ERA_SCORE_PER_ARMY_KILLED",
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
		"COMMEMORATION_MILITARY_QUEST_ARMY",
		"Amount",
		2
	);
	
```

