---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_TRADE_ROUTE_YIELD_PER_FOLLOWER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_TRADE_ROUTE_YIELD_PER_FOLLOWER
>
> * Class: `Unknown`
> * Parameters:
>	* Amount `Unknown`
>	* YieldType `Unknown`

## Samples

```SQL {title="MINOR_CIV_CHINGUETTI_FAITH_FOLLOWERS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"MINOR_CIV_CHINGUETTI_FAITH_FOLLOWERS",
		"MODIFIER_PLAYER_ADJUST_TRADE_ROUTE_YIELD_PER_FOLLOWER"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"MINOR_CIV_CHINGUETTI_FAITH_FOLLOWERS",
		"Amount",
		1
	),
	(
		"MINOR_CIV_CHINGUETTI_FAITH_FOLLOWERS",
		"YieldType",
		"YIELD_FAITH"
	);
	
```

