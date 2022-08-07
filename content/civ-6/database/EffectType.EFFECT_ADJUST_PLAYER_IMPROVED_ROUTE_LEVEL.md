---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_IMPROVED_ROUTE_LEVEL
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_IMPROVED_ROUTE_LEVEL
>
> * Class: `PLAYERS`
> * Parameters:
>	* ImprovedRouteLevel `Integer`

## Samples
```SQL {title="TRAIT_SATRAPIES_IMPROVED_ROUTE_LEVEL"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_SATRAPIES_IMPROVED_ROUTE_LEVEL",
		"MODIFIER_PLAYER_ADJUST_IMPROVED_ROUTE_LEVEL"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_SATRAPIES_IMPROVED_ROUTE_LEVEL",
		"ImprovedRouteLevel",
		1
	);
	
```

