---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_ERA_SCORE_PER_CULTURE_BUILDING_CONSTRUCTED
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_ERA_SCORE_PER_CULTURE_BUILDING_CONSTRUCTED
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="COMMEMORATION_CULTURAL_BUILDING_QUEST"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"COMMEMORATION_CULTURAL_BUILDING_QUEST",
		"MODIFIER_PLAYER_ADJUST_PLAYER_ERA_SCORE_PER_CULTURE_BUILDING_CONSTRUCTED",
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
		"COMMEMORATION_CULTURAL_BUILDING_QUEST",
		"Amount",
		1
	);
	
```

