---
tags:
- EffectType
title: EFFECT_ADJUST_BUILDING_YIELD_MODIFIER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_BUILDING_YIELD_MODIFIER
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`
>	* BuildingType `String`
>		* [Buildings.BuildingType]
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples

```SQL {title="TRAIT_DOUBLEMONUMENTCULTURE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_DOUBLEMONUMENTCULTURE",
		"MODIFIER_PLAYER_CITIES_ADJUST_BUILDING_YIELD_MODIFIER"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_DOUBLEMONUMENTCULTURE",
		"Amount",
		100
	),
	(
		"TRAIT_DOUBLEMONUMENTCULTURE",
		"BuildingType",
		"BUILDING_MONUMENT"
	),
	(
		"TRAIT_DOUBLEMONUMENTCULTURE",
		"YieldType",
		"YIELD_CULTURE"
	);
	
```

