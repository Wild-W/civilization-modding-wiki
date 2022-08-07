---
tags:
- EffectType
title: EFFECT_ADJUST_TRADE_ROUTE_YIELD_CHANGE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_TRADE_ROUTE_YIELD_CHANGE
>
> * Class: `TRADE ROUTES`
> * Parameters:
>	* AffectDestination `Boolean`
>	* AffectOrigin `Boolean`
>	* Amount `Integer`
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples
```SQL {title="ALLIANCE_ADD_SCIENCE_TO_DESTINATION_TRADE_ROUTE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"ALLIANCE_ADD_SCIENCE_TO_DESTINATION_TRADE_ROUTE",
		"MODIFIER_ALLIANCE_TRADE_ROUTE_ADJUST_YIELD",
		"ROUTE_BETWEEN_ALLIES_REQUIREMENTS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"ALLIANCE_ADD_SCIENCE_TO_DESTINATION_TRADE_ROUTE",
		"AffectDestination",
		1
	),
	(
		"ALLIANCE_ADD_SCIENCE_TO_DESTINATION_TRADE_ROUTE",
		"Amount",
		1
	),
	(
		"ALLIANCE_ADD_SCIENCE_TO_DESTINATION_TRADE_ROUTE",
		"YieldType",
		"YIELD_SCIENCE"
	);
	
```

```SQL {title="ALLIANCE_ADD_SCIENCE_TO_ORIGIN_TRADE_ROUTE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"ALLIANCE_ADD_SCIENCE_TO_ORIGIN_TRADE_ROUTE",
		"MODIFIER_ALLIANCE_TRADE_ROUTE_ADJUST_YIELD",
		"ROUTE_BETWEEN_ALLIES_REQUIREMENTS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"ALLIANCE_ADD_SCIENCE_TO_ORIGIN_TRADE_ROUTE",
		"AffectOrigin",
		1
	),
	(
		"ALLIANCE_ADD_SCIENCE_TO_ORIGIN_TRADE_ROUTE",
		"Amount",
		2
	),
	(
		"ALLIANCE_ADD_SCIENCE_TO_ORIGIN_TRADE_ROUTE",
		"YieldType",
		"YIELD_SCIENCE"
	);
	
```

