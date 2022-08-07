---
tags:
- EffectType
title: EFFECT_ADJUST_RELIGIOUS_SPREAD_DISTANCE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_RELIGIOUS_SPREAD_DISTANCE
>
> * Class: `PLAYERS`
> * Parameters:
>	* DistanceChange `Integer`

## Samples

```SQL {title="ITINERANT_PREACHERS_SPREAD_DISTANCE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"ITINERANT_PREACHERS_SPREAD_DISTANCE",
		"MODIFIER_PLAYER_RELIGION_ADJUST_RELIGIOUS_SPREAD_DISTANCE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"ITINERANT_PREACHERS_SPREAD_DISTANCE",
		"DistanceChange",
		3
	);
	
```

