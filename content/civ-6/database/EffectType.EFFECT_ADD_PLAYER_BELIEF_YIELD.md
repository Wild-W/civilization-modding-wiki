---
tags:
- EffectType
title: EFFECT_ADD_PLAYER_BELIEF_YIELD
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADD_PLAYER_BELIEF_YIELD
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`
>	* BeliefYieldType `String`
>		* BELIEF_YIELD_PER_CITY>		  BELIEF_YIELD_PER_DISTRICT>		  BELIEF_YIELD_PER_FOLLOWER>		  BELIEF_YIELD_PER_FOREIGN_CITY>		  BELIEF_YIELD_PER_FOREIGN_FOLLOWER
>	* PerXItems `Integer`
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples
```SQL {title="TRAIT_SCIENCE_PER_FOREIGN_CITY_FOLLOWING_RELIGION"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_SCIENCE_PER_FOREIGN_CITY_FOLLOWING_RELIGION",
		"MODIFIER_PLAYER_RELIGION_ADD_PLAYER_BELIEF_YIELD"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_SCIENCE_PER_FOREIGN_CITY_FOLLOWING_RELIGION",
		"Amount",
		1
	),
	(
		"TRAIT_SCIENCE_PER_FOREIGN_CITY_FOLLOWING_RELIGION",
		"BeliefYieldType",
		"BELIEF_YIELD_PER_FOREIGN_CITY"
	),
	(
		"TRAIT_SCIENCE_PER_FOREIGN_CITY_FOLLOWING_RELIGION",
		"PerXItems",
		1
	),
	(
		"TRAIT_SCIENCE_PER_FOREIGN_CITY_FOLLOWING_RELIGION",
		"YieldType",
		"YIELD_SCIENCE"
	);
	
```

