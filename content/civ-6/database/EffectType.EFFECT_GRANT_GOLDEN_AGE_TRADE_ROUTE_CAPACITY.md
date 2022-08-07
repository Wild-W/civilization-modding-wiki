---
tags:
- EffectType
title: EFFECT_GRANT_GOLDEN_AGE_TRADE_ROUTE_CAPACITY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_GRANT_GOLDEN_AGE_TRADE_ROUTE_CAPACITY
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="GOLDEN_AGE_TRADE_ROUTE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"GOLDEN_AGE_TRADE_ROUTE",
		"MODIFIER_PLAYER_ADJUST_TRADE_ROUTE_CAPACITY_GOLDEN_AGE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"GOLDEN_AGE_TRADE_ROUTE",
		"Amount",
		1
	);
	
```

