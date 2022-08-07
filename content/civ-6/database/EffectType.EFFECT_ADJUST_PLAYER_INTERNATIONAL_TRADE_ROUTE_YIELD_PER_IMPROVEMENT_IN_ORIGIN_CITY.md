---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_INTERNATIONAL_TRADE_ROUTE_YIELD_PER_IMPROVEMENT_IN_ORIGIN_CITY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_INTERNATIONAL_TRADE_ROUTE_YIELD_PER_IMPROVEMENT_IN_ORIGIN_CITY
>
> * Class: `Unknown`
> * Parameters:
>	* Amount `Unknown`
>	* ImprovementType `Unknown`
>	* YieldType `Unknown`

## Samples
```SQL {title="MINOR_CIV_SAMARKAND_TRADE_GOLD_MODIFIER"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"MINOR_CIV_SAMARKAND_TRADE_GOLD_MODIFIER",
		"MODIFIER_PLAYER_ADJUST_TRADE_ROUTE_YIELD_PER_IMPROVEMENT_AT_LOCATION_BABYLON"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"MINOR_CIV_SAMARKAND_TRADE_GOLD_MODIFIER",
		"Amount",
		1
	),
	(
		"MINOR_CIV_SAMARKAND_TRADE_GOLD_MODIFIER",
		"ImprovementType",
		"IMPROVEMENT_TRADING_DOME"
	),
	(
		"MINOR_CIV_SAMARKAND_TRADE_GOLD_MODIFIER",
		"YieldType",
		"YIELD_GOLD"
	);
	
```

