---
tags:
- EffectType
title: EFFECT_ENABLE_SPECIFIC_BUILDING_FAITH_PURCHASE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ENABLE_SPECIFIC_BUILDING_FAITH_PURCHASE
>
> * Class: `CITIES`
> * Parameters:
>	* BuildingType `String`
>		* [Buildings.BuildingType]

## Samples

```SQL {title="TRAIT_FAITH_MUSEUM_ARTIFACT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_FAITH_MUSEUM_ARTIFACT",
		"MODIFIER_PLAYER_CITIES_ENABLE_SPECIFIC_BUILDING_FAITH_PURCHASE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_FAITH_MUSEUM_ARTIFACT",
		"BuildingType",
		"BUILDING_MUSEUM_ARTIFACT"
	);
	
```

