---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_IDENTITY_PER_TURN_FOR_DOMESTIC_TRADE_ROUTE_ORIGIN
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_IDENTITY_PER_TURN_FOR_DOMESTIC_TRADE_ROUTE_ORIGIN
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="TRAIT_IDENTITY_FROM_DOMESTIC_TRADE_ROUTES"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_IDENTITY_FROM_DOMESTIC_TRADE_ROUTES",
		"MODIFIER_PLAYER_ADJUST_PLAYER_IDENTITY_PER_TURN_FOR_DOMESTIC_TRADE_ROUTE_ORIGIN"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_IDENTITY_FROM_DOMESTIC_TRADE_ROUTES",
		"Amount",
		2
	);
	
```

