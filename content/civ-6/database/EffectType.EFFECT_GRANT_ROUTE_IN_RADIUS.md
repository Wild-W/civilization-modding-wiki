---
tags:
- EffectType
title: EFFECT_GRANT_ROUTE_IN_RADIUS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_GRANT_ROUTE_IN_RADIUS
>
> * Class: `Unknown`
> * Parameters:
>	* Radius `Integer`
>	* RouteType `String`
>		* [Routes.RouteType]

## Samples

```SQL {title="GOLDENGATE_GRANT_ROUTES"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"GOLDENGATE_GRANT_ROUTES",
		"MODIFIER_GRANT_ROUTE_IN_RADIUS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"GOLDENGATE_GRANT_ROUTES",
		"Radius",
		1
	),
	(
		"GOLDENGATE_GRANT_ROUTES",
		"RouteType",
		"ROUTE_MODERN_ROAD"
	);
	
```

