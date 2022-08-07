---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_IMMEDIATE_TRADING_POST
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_IMMEDIATE_TRADING_POST
>
> * Class: `PLAYERS`
> * Parameters:
>	* ImmediateTradingPost `Boolean`

## Samples
```SQL {title="TRAIT_IMMEDIATE_TRADING_POST"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_IMMEDIATE_TRADING_POST",
		"MODIFIER_PLAYER_ADJUST_IMMEDIATE_TRADING_POST"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_IMMEDIATE_TRADING_POST",
		"ImmediateTradingPost",
		1
	);
	
```

