---
tags:
- EffectType
title: EFFECT_ADJUST_DISTRICT_TOURISM_ADJACENCY_YIELD_MOFIFIER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_DISTRICT_TOURISM_ADJACENCY_YIELD_MOFIFIER
>
> * Class: `DISTRICTS`
> * Parameters:
>	* Amount `Unknown`
>	* YieldType `Unknown`

## Samples

```SQL {title="THANH_TOURISM_CULTURE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"THANH_TOURISM_CULTURE",
		"MODIFIER_PLAYER_DISTRICT_ADJUST_TOURISM_ADJACENCY_YIELD_MOFIFIER",
		"THANH_PLAYER_HAS_FLIGHT_REQUIREMENTS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"THANH_TOURISM_CULTURE",
		"Amount",
		100
	),
	(
		"THANH_TOURISM_CULTURE",
		"YieldType",
		"YIELD_CULTURE"
	);
	
```

