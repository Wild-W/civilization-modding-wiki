---
tags:
- EffectType
title: EFFECT_ADJUST_TRADE_ROUTE_CAPACITY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_TRADE_ROUTE_CAPACITY
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="COLOSSUS_ADDTRADEROUTE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"COLOSSUS_ADDTRADEROUTE",
		"MODIFIER_PLAYER_ADJUST_TRADE_ROUTE_CAPACITY"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"COLOSSUS_ADDTRADEROUTE",
		"Amount",
		1
	);
	
```

