---
tags:
- EffectType
title: EFFECT_ADJUST_RANDOM_EVENT_MODIFIED_DAMAGE_OPPOSING_PLAYER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_RANDOM_EVENT_MODIFIED_DAMAGE_OPPOSING_PLAYER
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`
>	* RandomEventType `String`

## Samples
```SQL {title="TRAIT_BLIZZARD_DOUBLE_DAMAGE_SIGNIFICANT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_BLIZZARD_DOUBLE_DAMAGE_SIGNIFICANT",
		"MODIFIER_PLAYER_ADJUST_RANDOM_EVENT_MODIFIED_DAMAGE_OPPOSING_PLAYER"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_BLIZZARD_DOUBLE_DAMAGE_SIGNIFICANT",
		"Amount",
		100
	),
	(
		"TRAIT_BLIZZARD_DOUBLE_DAMAGE_SIGNIFICANT",
		"RandomEventType",
		"RANDOM_EVENT_BLIZZARD_SIGNIFICANT"
	);
	
```

