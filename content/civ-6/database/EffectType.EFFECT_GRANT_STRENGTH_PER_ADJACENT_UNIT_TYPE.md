---
tags:
- EffectType
title: EFFECT_GRANT_STRENGTH_PER_ADJACENT_UNIT_TYPE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_GRANT_STRENGTH_PER_ADJACENT_UNIT_TYPE
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`
>	* UnitType `String`

## Samples
```SQL {title="LLANERO_ADJACENCY_STRENGTH"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		OwnerRequirementSetId
	)
VALUES
	(
		"LLANERO_ADJACENCY_STRENGTH",
		"GRANT_STRENGTH_PER_ADJACENT_UNIT_TYPE",
		"LLANERO_IS_ADJACENT_REQUIREMENTS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"LLANERO_ADJACENCY_STRENGTH",
		"Amount",
		2
	),
	(
		"LLANERO_ADJACENCY_STRENGTH",
		"UnitType",
		"UNIT_COLOMBIAN_LLANERO"
	);
	
```

