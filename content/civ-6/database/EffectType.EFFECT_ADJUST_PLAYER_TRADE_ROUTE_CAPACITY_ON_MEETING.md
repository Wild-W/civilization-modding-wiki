---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_TRADE_ROUTE_CAPACITY_ON_MEETING
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_TRADE_ROUTE_CAPACITY_ON_MEETING
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Unknown`

## Samples

```SQL {title="TRAIT_JOAO_TRADE_ROUTE_ON_MEET"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_JOAO_TRADE_ROUTE_ON_MEET",
		"MODIFIER_PLAYER_ADJUST_TRADE_ROUTE_CAPACITY_ON_MEETING"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_JOAO_TRADE_ROUTE_ON_MEET",
		"Amount",
		1
	);
	
```

