---
tags:
- EffectType
title: EFFECT_ADJUST_RANDOM_EVENT_NO_UNIT_DAMAGE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_RANDOM_EVENT_NO_UNIT_DAMAGE
>
> * Class: `PLAYERS`
> * Parameters:
>	* NoDamage `Boolean`
>	* RandomEventType `String`
>		* [RandomEvents.RandomEventType]

## Samples
```SQL {title="TRAIT_BLIZZARD_PREVENTION_SIGNIFICANT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_BLIZZARD_PREVENTION_SIGNIFICANT",
		"MODIFIER_PLAYER_ADJUST_RANDOM_EVENT_NO_UNIT_DAMAGE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_BLIZZARD_PREVENTION_SIGNIFICANT",
		"NoDamage",
		1
	),
	(
		"TRAIT_BLIZZARD_PREVENTION_SIGNIFICANT",
		"RandomEventType",
		"RANDOM_EVENT_BLIZZARD_SIGNIFICANT"
	);
	
```

