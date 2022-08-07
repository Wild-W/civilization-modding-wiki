---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_ALWAYS_ALLOW_COMMEMORATION_QUEST_COUNT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_ALWAYS_ALLOW_COMMEMORATION_QUEST_COUNT
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="TRAIT_ALLOW_QUESTS_IN_GOLDEN_AGE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_ALLOW_QUESTS_IN_GOLDEN_AGE",
		"MODIFIER_PLAYER_ADJUST_PLAYER_ALWAYS_ALLOW_COMMEMORATION_QUEST_COUNT"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_ALLOW_QUESTS_IN_GOLDEN_AGE",
		"Amount",
		1
	);
	
```

