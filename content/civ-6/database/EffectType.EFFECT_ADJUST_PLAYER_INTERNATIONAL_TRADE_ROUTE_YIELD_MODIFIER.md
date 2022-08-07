---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_INTERNATIONAL_TRADE_ROUTE_YIELD_MODIFIER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_INTERNATIONAL_TRADE_ROUTE_YIELD_MODIFIER
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`
>	* YieldType `Unknown`

## Samples

```SQL {title="TRAIT_INTERNATIONAL_TRADE_GAIN_ALL_YIELDS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_INTERNATIONAL_TRADE_GAIN_ALL_YIELDS",
		"MODIFIER_PLAYER_ADJUST_INTERNATIONAL_TRADE_ROUTE_YIELD_MODIFIER"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_INTERNATIONAL_TRADE_GAIN_ALL_YIELDS",
		"Amount",
		"50, 50, 50, 50, 50, 50"
	),
	(
		"TRAIT_INTERNATIONAL_TRADE_GAIN_ALL_YIELDS",
		"YieldType",
		"YIELD_PRODUCTION, YIELD_FOOD, YIELD_SCIENCE, YIELD_CULTURE, YIELD_GOLD, YIELD_FAITH"
	);
	
```

