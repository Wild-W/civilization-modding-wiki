---
tags:
- EffectType
title: EFFECT_ADD_RELIGIOUS_BELIEF_YIELD
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADD_RELIGIOUS_BELIEF_YIELD
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`
>	* BeliefYieldType `String`
>		* BELIEF_YIELD_PER_CITY>		  BELIEF_YIELD_PER_DISTRICT>		  BELIEF_YIELD_PER_FOLLOWER>		  BELIEF_YIELD_PER_FOREIGN_CITY>		  BELIEF_YIELD_PER_FOREIGN_FOLLOWER
>	* DistrictType `String`
>		* [Districts.DistrictType]
>	* PerXItems `Integer`
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples
```SQL {title="CHURCH_PROPERTY_GOLD_CITY_MODIFIER"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"CHURCH_PROPERTY_GOLD_CITY_MODIFIER",
		"MODIFIER_PLAYER_RELIGION_ADD_RELIGIOUS_BELIEF_YIELD"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"CHURCH_PROPERTY_GOLD_CITY_MODIFIER",
		"Amount",
		2
	),
	(
		"CHURCH_PROPERTY_GOLD_CITY_MODIFIER",
		"BeliefYieldType",
		"BELIEF_YIELD_PER_CITY"
	),
	(
		"CHURCH_PROPERTY_GOLD_CITY_MODIFIER",
		"PerXItems",
		1
	),
	(
		"CHURCH_PROPERTY_GOLD_CITY_MODIFIER",
		"YieldType",
		"YIELD_GOLD"
	);
	
```

```SQL {title="LAY_MINISTRY_CULTURE_DISTRICTS_MODIFIER"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"LAY_MINISTRY_CULTURE_DISTRICTS_MODIFIER",
		"MODIFIER_PLAYER_RELIGION_ADD_RELIGIOUS_BELIEF_YIELD"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"LAY_MINISTRY_CULTURE_DISTRICTS_MODIFIER",
		"Amount",
		1
	),
	(
		"LAY_MINISTRY_CULTURE_DISTRICTS_MODIFIER",
		"BeliefYieldType",
		"BELIEF_YIELD_PER_DISTRICT"
	),
	(
		"LAY_MINISTRY_CULTURE_DISTRICTS_MODIFIER",
		"DistrictType",
		"DISTRICT_THEATER"
	),
	(
		"LAY_MINISTRY_CULTURE_DISTRICTS_MODIFIER",
		"PerXItems",
		1
	),
	(
		"LAY_MINISTRY_CULTURE_DISTRICTS_MODIFIER",
		"YieldType",
		"YIELD_CULTURE"
	);
	
```

