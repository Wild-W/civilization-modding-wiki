---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_ALLIANCE_FAVOR_MULTIPLIER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_ALLIANCE_FAVOR_MULTIPLIER
>
> * Class: `Unknown`
> * Parameters:
>	* Amount `Unknown`

## Samples

```SQL {title="POLICY_POPULAR_FRONT_ALLIANCE_FAVOR"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"POLICY_POPULAR_FRONT_ALLIANCE_FAVOR",
		"MODIFIER_PLAYER_ADJUST_ALLIANCE_FAVOR_MULTIPLIER"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"POLICY_POPULAR_FRONT_ALLIANCE_FAVOR",
		"Amount",
		100
	);
	
```

