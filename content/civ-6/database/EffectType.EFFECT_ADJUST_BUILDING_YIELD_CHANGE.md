---
tags:
- EffectType
title: EFFECT_ADJUST_BUILDING_YIELD_CHANGE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_BUILDING_YIELD_CHANGE
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`
>	* BuildingType `String`
>		* [Buildings.BuildingType]
>	* CityStatesOnly `Boolean`
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples

```SQL {title="FEED_THE_WORLD_SHRINE_FOOD_MODIFIER"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"FEED_THE_WORLD_SHRINE_FOOD_MODIFIER",
		"MODIFIER_BUILDING_YIELD_CHANGE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"FEED_THE_WORLD_SHRINE_FOOD_MODIFIER",
		"Amount",
		2
	),
	(
		"FEED_THE_WORLD_SHRINE_FOOD_MODIFIER",
		"BuildingType",
		"BUILDING_SHRINE"
	),
	(
		"FEED_THE_WORLD_SHRINE_FOOD_MODIFIER",
		"YieldType",
		"YIELD_FOOD"
	);
	
```


```SQL {title="MINOR_CIV_SCIENTIFIC_YIELD_FOR_LIBRARY"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"MINOR_CIV_SCIENTIFIC_YIELD_FOR_LIBRARY",
		"MODIFIER_PLAYER_CITIES_ADJUST_BUILDING_YIELD_CHANGE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"MINOR_CIV_SCIENTIFIC_YIELD_FOR_LIBRARY",
		"Amount",
		2
	),
	(
		"MINOR_CIV_SCIENTIFIC_YIELD_FOR_LIBRARY",
		"BuildingType",
		"BUILDING_LIBRARY"
	),
	(
		"MINOR_CIV_SCIENTIFIC_YIELD_FOR_LIBRARY",
		"CityStatesOnly",
		1
	),
	(
		"MINOR_CIV_SCIENTIFIC_YIELD_FOR_LIBRARY",
		"YieldType",
		"YIELD_SCIENCE"
	);
	
```

