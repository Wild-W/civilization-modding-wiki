---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_TRADE_ROUTE_RELIGIOUS_PRESSURE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_TRADE_ROUTE_RELIGIOUS_PRESSURE
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`
>	* Destination `Boolean`
>	* Origin `Boolean`

## Samples

```SQL {title="TRAIT_ORIGIN_DESTINATION_RELIGIOUS_PRESSURE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_ORIGIN_DESTINATION_RELIGIOUS_PRESSURE",
		"MODIFIER_PLAYER_ADJUST_TRADE_ROUTE_RELIGIOUS_PRESSURE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_ORIGIN_DESTINATION_RELIGIOUS_PRESSURE",
		"Amount",
		100
	),
	(
		"TRAIT_ORIGIN_DESTINATION_RELIGIOUS_PRESSURE",
		"Destination",
		1
	),
	(
		"TRAIT_ORIGIN_DESTINATION_RELIGIOUS_PRESSURE",
		"Origin",
		1
	);
	
```

