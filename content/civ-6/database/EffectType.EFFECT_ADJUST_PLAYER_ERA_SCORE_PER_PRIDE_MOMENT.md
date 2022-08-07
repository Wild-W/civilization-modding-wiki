---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_ERA_SCORE_PER_PRIDE_MOMENT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_ERA_SCORE_PER_PRIDE_MOMENT
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`
>	* MinScore `Integer`

## Samples

```SQL {title="TAJ_MAHAL_EXTRA_ERA_SCORE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TAJ_MAHAL_EXTRA_ERA_SCORE",
		"MODIFIER_PLAYER_ADJUST_PLAYER_ERA_SCORE_PER_PRIDE_MOMENT"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TAJ_MAHAL_EXTRA_ERA_SCORE",
		"Amount",
		1
	),
	(
		"TAJ_MAHAL_EXTRA_ERA_SCORE",
		"MinScore",
		2
	);
	
```

