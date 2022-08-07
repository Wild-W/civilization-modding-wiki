---
tags:
- EffectType
title: EFFECT_GRANT_CITY_YIELD_PERCENT_BUILDING_CREATED_COST
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_GRANT_CITY_YIELD_PERCENT_BUILDING_CREATED_COST
>
> * Class: `CITIES`
> * Parameters:
>	* BuildingProductionPercent `Integer`
>	* IncludeWonder `Boolean`
>	* YieldType `String`

## Samples
```SQL {title="CARDINAL_CITADEL_OF_GOD_FAITH_FINISH_BUILDINGS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"CARDINAL_CITADEL_OF_GOD_FAITH_FINISH_BUILDINGS",
		"MODIFIER_SINGLE_CITY_GRANT_YIELD_PER_BUILDING_COST"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"CARDINAL_CITADEL_OF_GOD_FAITH_FINISH_BUILDINGS",
		"BuildingProductionPercent",
		25
	),
	(
		"CARDINAL_CITADEL_OF_GOD_FAITH_FINISH_BUILDINGS",
		"IncludeWonder",
		0
	),
	(
		"CARDINAL_CITADEL_OF_GOD_FAITH_FINISH_BUILDINGS",
		"YieldType",
		"YIELD_FAITH"
	);
	
```

