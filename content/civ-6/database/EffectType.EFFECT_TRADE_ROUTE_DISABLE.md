---
tags:
- EffectType
title: EFFECT_TRADE_ROUTE_DISABLE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_TRADE_ROUTE_DISABLE
>
> * Class: `Unknown`
> * Parameters:
>	* Domestic `Boolean`
>	* InternationalMajors `Boolean`
>	* InternationalMinors `Boolean`

## Samples
```SQL {title="INTERNATIONAL_MAJOR_TRADE_ROUTES_DISABLED"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"INTERNATIONAL_MAJOR_TRADE_ROUTES_DISABLED",
		"MODIFIER_PLAYER_TRADE_ROUTES_DISABLE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"INTERNATIONAL_MAJOR_TRADE_ROUTES_DISABLED",
		"Domestic",
		0
	),
	(
		"INTERNATIONAL_MAJOR_TRADE_ROUTES_DISABLED",
		"InternationalMajors",
		1
	),
	(
		"INTERNATIONAL_MAJOR_TRADE_ROUTES_DISABLED",
		"InternationalMinors",
		0
	);
	
```

