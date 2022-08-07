---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_TRADE_ROUTE_YIELD_PER_LOCAL_BONUS_RESOURCE_FOR_INTERNATIONAL
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_TRADE_ROUTE_YIELD_PER_LOCAL_BONUS_RESOURCE_FOR_INTERNATIONAL
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples

```SQL {title="GREAT_ZIMBABWE_INTERNATIONALBONUSRESOURCEGOLD"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"GREAT_ZIMBABWE_INTERNATIONALBONUSRESOURCEGOLD",
		"MODIFIER_PLAYER_CITY_TRADE_ROUTE_YIELD_PER_LOCAL_BONUS_RESOURCE_FOR_INTERNATIONAL"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"GREAT_ZIMBABWE_INTERNATIONALBONUSRESOURCEGOLD",
		"Amount",
		2
	),
	(
		"GREAT_ZIMBABWE_INTERNATIONALBONUSRESOURCEGOLD",
		"YieldType",
		"YIELD_GOLD"
	);
	
```

