---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_TOKEN_ON_TRADE_ROUTE_STARTED
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_TOKEN_ON_TRADE_ROUTE_STARTED
>
> * Class: `Unknown`
> * Parameters:
>	* Amount `Unknown`

## Samples
```SQL {title="GOVERNOR_PROMOTION_OWLS_OF_MINERVA_1_ENVOY_FROM_TRADE_ROUTE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"GOVERNOR_PROMOTION_OWLS_OF_MINERVA_1_ENVOY_FROM_TRADE_ROUTE",
		"MODIFIER_PLAYER_ADJUST_TOKEN_ON_TRADE_ROUTE_STARTED"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"GOVERNOR_PROMOTION_OWLS_OF_MINERVA_1_ENVOY_FROM_TRADE_ROUTE",
		"Amount",
		1
	);
	
```

