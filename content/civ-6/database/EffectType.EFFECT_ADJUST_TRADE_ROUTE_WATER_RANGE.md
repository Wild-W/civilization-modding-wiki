---
tags:
- EffectType
title: EFFECT_ADJUST_TRADE_ROUTE_WATER_RANGE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_TRADE_ROUTE_WATER_RANGE
>
> * Class: `Unknown`
> * Parameters:
>	* Amount `Unknown`

## Samples

```SQL {title="TRAIT_WATER_TRADE_ROUTE_RANGE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_WATER_TRADE_ROUTE_RANGE",
		"MODIFIER_PLAYER_ADJUST_TRADE_ROUTE_WATER_RANGE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_WATER_TRADE_ROUTE_RANGE",
		"Amount",
		15
	);
	
```

