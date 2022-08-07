---
tags:
- EffectType
title: EFFECT_ADJUST_GAINS_ALL_FOLLOWER_BELIEFS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_GAINS_ALL_FOLLOWER_BELIEFS
>
> * Class: `PLAYERS`
> * Parameters:
>	* Enable `Boolean`

## Samples

```SQL {title="TRAIT_GAINS_ALL_FOLLOWER_BELIEFS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_GAINS_ALL_FOLLOWER_BELIEFS",
		"MODIFIER_PLAYER_GAINS_ALL_FOLLOWER_BELIEFS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_GAINS_ALL_FOLLOWER_BELIEFS",
		"Enable",
		1
	);
	
```

