---
tags:
- EffectType
title: EFFECT_GRANT_PLAYER_YIELD_PERCENT_UNIT_COST
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_GRANT_PLAYER_YIELD_PERCENT_UNIT_COST
>
> * Class: `PLAYERS`
> * Parameters:
>	* UnitCostPercent `Integer`
>		* [Technologies.TechnologyType]
>	* YieldType `String`
>		* [Technologies.TechnologyType]

## Samples

```SQL {title="GREAT_PERSON_INDIVIDUAL_COMMANDANTE_UNIT_GOLD"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent
	)
VALUES
	(
		"GREAT_PERSON_INDIVIDUAL_COMMANDANTE_UNIT_GOLD",
		"MODIFIER_PLAYER_GRANT_YIELD_PERCENT_UNIT_COST",
		1,
		1
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"GREAT_PERSON_INDIVIDUAL_COMMANDANTE_UNIT_GOLD",
		"UnitCostPercent",
		50
	),
	(
		"GREAT_PERSON_INDIVIDUAL_COMMANDANTE_UNIT_GOLD",
		"YieldType",
		"YIELD_GOLD"
	);
	
```

