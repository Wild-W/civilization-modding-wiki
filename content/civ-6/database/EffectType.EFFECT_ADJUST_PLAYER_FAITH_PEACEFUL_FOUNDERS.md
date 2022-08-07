---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_FAITH_PEACEFUL_FOUNDERS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_FAITH_PEACEFUL_FOUNDERS
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="TRAIT_FAITH_PEACEFUL_FOUNDERS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_FAITH_PEACEFUL_FOUNDERS",
		"MODIFIER_PLAYER_ADJUST_FAITH_PEACEFUL_FOUNDERS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_FAITH_PEACEFUL_FOUNDERS",
		"Amount",
		5
	);
	
```

