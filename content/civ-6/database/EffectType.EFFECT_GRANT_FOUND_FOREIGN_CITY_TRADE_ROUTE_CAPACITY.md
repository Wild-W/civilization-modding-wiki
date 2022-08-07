---
tags:
- EffectType
title: EFFECT_GRANT_FOUND_FOREIGN_CITY_TRADE_ROUTE_CAPACITY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_GRANT_FOUND_FOREIGN_CITY_TRADE_ROUTE_CAPACITY
>
> * Class: `Unknown`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="TRAIT_FOREIGN_CONTINENT_TRADE_ROUTE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_FOREIGN_CONTINENT_TRADE_ROUTE",
		"MODIFIER_PLAYER_ADJUST_TRADE_ROUTE_CAPACITY_FOUND_FOREIGN_CITY"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_FOREIGN_CONTINENT_TRADE_ROUTE",
		"Amount",
		1
	);
	
```

