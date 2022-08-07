---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_RANDOM_EVENT_AVOID
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_RANDOM_EVENT_AVOID
>
> * Class: `PLAYERS`
> * Parameters:
>	* RandomEventType `String`
>		* [RandomEvents.RandomEventType]

## Samples

```SQL {title="TRAIT_AVOID_MODERATE_FLOOD"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_AVOID_MODERATE_FLOOD",
		"MODIFIER_PLAYER_ADJUST_AVOID_RANDOM_EVENT"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_AVOID_MODERATE_FLOOD",
		"RandomEventType",
		"RANDOM_EVENT_FLOOD_MODERATE"
	);
	
```

