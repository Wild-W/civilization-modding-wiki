---
tags:
- EffectType
title: EFFECT_ALLIANCE_ENVOY_POINTS_FROM_ALLY_TRIBUTARIES
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ALLIANCE_ENVOY_POINTS_FROM_ALLY_TRIBUTARIES
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="ALLIANCE_ENVOY_POINTS_FROM_ALLIANCE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"ALLIANCE_ENVOY_POINTS_FROM_ALLIANCE",
		"MODIFIER_ALLIANCE_PLAYERS_ENVOY_POINTS_FROM_ALLY"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"ALLIANCE_ENVOY_POINTS_FROM_ALLIANCE",
		"Amount",
		1
	);
	
```

