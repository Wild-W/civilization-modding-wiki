---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_YIELD_CHANGE_PER_USED_INFLUENCE_TOKEN
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_YIELD_CHANGE_PER_USED_INFLUENCE_TOKEN
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples
```SQL {title="MERCHANTCONFEDERATION_INFLUENCETOKENGOLD"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"MERCHANTCONFEDERATION_INFLUENCETOKENGOLD",
		"MODIFIER_PLAYER_ADJUST_YIELD_CHANGE_PER_USED_INFLUENCE_TOKEN"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"MERCHANTCONFEDERATION_INFLUENCETOKENGOLD",
		"Amount",
		1
	),
	(
		"MERCHANTCONFEDERATION_INFLUENCETOKENGOLD",
		"YieldType",
		"YIELD_GOLD"
	);
	
```

