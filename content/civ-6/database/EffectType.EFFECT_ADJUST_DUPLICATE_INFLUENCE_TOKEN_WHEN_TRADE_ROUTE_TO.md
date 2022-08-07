---
tags:
- EffectType
title: EFFECT_ADJUST_DUPLICATE_INFLUENCE_TOKEN_WHEN_TRADE_ROUTE_TO
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_DUPLICATE_INFLUENCE_TOKEN_WHEN_TRADE_ROUTE_TO
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`
>		* Amount of envoys

## Samples
```SQL {title="TRAIT_ROOSEVELT_COROLLARY_TRADE_ROUTE_TOKEN"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_ROOSEVELT_COROLLARY_TRADE_ROUTE_TOKEN",
		"MODIFIER_PLAYER_ADJUST_DUPLICATE_INFLUENCE_TOKEN_WHEN_TRADE_ROUTE_TO"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_ROOSEVELT_COROLLARY_TRADE_ROUTE_TOKEN",
		"Amount",
		1
	);
	
```

