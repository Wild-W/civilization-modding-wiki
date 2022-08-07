---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_TRADE_ROUTE_YIELD_MODIFIER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_TRADE_ROUTE_YIELD_MODIFIER
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`
>	* Destination `Boolean`
>	* Origin `Boolean`
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples

```SQL {title="LETTEROFMARQUE_TRADE_ROUTE_YIELD_DROP_DEST_CULTURE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"LETTEROFMARQUE_TRADE_ROUTE_YIELD_DROP_DEST_CULTURE",
		"MODIFIER_PLAYER_ADJUST_TRADE_ROUTE_YIELD_MODIFIER"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"LETTEROFMARQUE_TRADE_ROUTE_YIELD_DROP_DEST_CULTURE",
		"Amount",
		"-50"
	),
	(
		"LETTEROFMARQUE_TRADE_ROUTE_YIELD_DROP_DEST_CULTURE",
		"Destination",
		1
	),
	(
		"LETTEROFMARQUE_TRADE_ROUTE_YIELD_DROP_DEST_CULTURE",
		"YieldType",
		"YIELD_CULTURE"
	);
	
```


```SQL {title="LETTEROFMARQUE_TRADE_ROUTE_YIELD_DROP_ORIG_CULTURE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"LETTEROFMARQUE_TRADE_ROUTE_YIELD_DROP_ORIG_CULTURE",
		"MODIFIER_PLAYER_ADJUST_TRADE_ROUTE_YIELD_MODIFIER"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"LETTEROFMARQUE_TRADE_ROUTE_YIELD_DROP_ORIG_CULTURE",
		"Amount",
		"-50"
	),
	(
		"LETTEROFMARQUE_TRADE_ROUTE_YIELD_DROP_ORIG_CULTURE",
		"Origin",
		1
	),
	(
		"LETTEROFMARQUE_TRADE_ROUTE_YIELD_DROP_ORIG_CULTURE",
		"YieldType",
		"YIELD_CULTURE"
	);
	
```

