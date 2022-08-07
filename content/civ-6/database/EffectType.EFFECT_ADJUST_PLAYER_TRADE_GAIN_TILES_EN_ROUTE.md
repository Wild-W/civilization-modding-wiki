---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_TRADE_GAIN_TILES_EN_ROUTE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_TRADE_GAIN_TILES_EN_ROUTE
>
> * Class: `PLAYERS`
> * Parameters:
>	* GainTileRadius `Integer`

## Samples

```SQL {title="TRAIT_TRADE_GAIN_TILES_EN_ROUTE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_TRADE_GAIN_TILES_EN_ROUTE",
		"MODIFIER_PLAYER_TRADE_GAIN_TILES_EN_ROUTE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_TRADE_GAIN_TILES_EN_ROUTE",
		"GainTileRadius",
		3
	);
	
```

