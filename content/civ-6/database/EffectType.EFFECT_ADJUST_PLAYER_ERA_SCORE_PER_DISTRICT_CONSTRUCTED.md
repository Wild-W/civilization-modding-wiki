---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_ERA_SCORE_PER_DISTRICT_CONSTRUCTED
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_ERA_SCORE_PER_DISTRICT_CONSTRUCTED
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="COMMEMORATION_INFRASTRUCTURE_QUEST"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"COMMEMORATION_INFRASTRUCTURE_QUEST",
		"MODIFIER_PLAYER_ADJUST_PLAYER_ERA_SCORE_PER_DISTRICT_CONSTRUCTED",
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
		"COMMEMORATION_INFRASTRUCTURE_QUEST",
		"Amount",
		1
	);
	
```
