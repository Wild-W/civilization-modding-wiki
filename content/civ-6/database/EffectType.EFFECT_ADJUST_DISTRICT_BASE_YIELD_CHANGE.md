---
tags:
- EffectType
title: EFFECT_ADJUST_DISTRICT_BASE_YIELD_CHANGE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_DISTRICT_BASE_YIELD_CHANGE
>
> * Class: `DISTRICTS`
> * Parameters:
>	* Amount `Integer`
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples

```SQL {title="ROYAL_NAVY_DOCKYARD_GOLD_FROM_FOREIGN_CONTINENT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"ROYAL_NAVY_DOCKYARD_GOLD_FROM_FOREIGN_CONTINENT",
		"MODIFIER_PLAYER_DISTRICT_ADJUST_BASE_YIELD_CHANGE",
		"DOCKYARD_FOREIGN_CONTINENT_REQUIREMENTS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"ROYAL_NAVY_DOCKYARD_GOLD_FROM_FOREIGN_CONTINENT",
		"Amount",
		2
	),
	(
		"ROYAL_NAVY_DOCKYARD_GOLD_FROM_FOREIGN_CONTINENT",
		"YieldType",
		"YIELD_GOLD"
	);
	
```

