---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_ADD_CHOP_YIELD
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_ADD_CHOP_YIELD
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples
```SQL {title="WC_RES_DEFORESTATION_GOLD"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"WC_RES_DEFORESTATION_GOLD",
		"MODIFIER_PLAYERS_ADD_CHOP_YIELD"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"WC_RES_DEFORESTATION_GOLD",
		"Amount",
		100
	),
	(
		"WC_RES_DEFORESTATION_GOLD",
		"YieldType",
		"YIELD_GOLD"
	);
	
```

