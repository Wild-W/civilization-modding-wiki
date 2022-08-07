---
tags:
- EffectType
title: EFFECT_ADJUST_RELIGIOUS_COMBAT_LOSS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_RELIGIOUS_COMBAT_LOSS
>
> * Class: `PLAYERS`
> * Parameters:
>	* ReductionPercent `Integer`

## Samples

```SQL {title="MONASTIC_ISOLATION_REDUCE_COMBAT_LOSS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"MONASTIC_ISOLATION_REDUCE_COMBAT_LOSS",
		"MODIFIER_PLAYER_RELIGION_ADJUST_COMBAT_LOSS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"MONASTIC_ISOLATION_REDUCE_COMBAT_LOSS",
		"ReductionPercent",
		100
	);
	
```

