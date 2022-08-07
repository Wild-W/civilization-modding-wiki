---
tags:
- EffectType
title: EFFECT_ADJUST_GAINS_FOUNDER_BELIEF_MAJORITY_RELIGION
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_GAINS_FOUNDER_BELIEF_MAJORITY_RELIGION
>
> * Class: `PLAYERS`
> * Parameters:
>	* Enable `Boolean`

## Samples

```SQL {title="TRAIT_GAINS_FOUNDER_BELIEF_MAJORITY_RELIGION"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_GAINS_FOUNDER_BELIEF_MAJORITY_RELIGION",
		"MODIFIER_PLAYER_GAINS_FOUNDER_BELIEF_MAJORITY_RELIGION"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_GAINS_FOUNDER_BELIEF_MAJORITY_RELIGION",
		"Enable",
		1
	);
	
```

