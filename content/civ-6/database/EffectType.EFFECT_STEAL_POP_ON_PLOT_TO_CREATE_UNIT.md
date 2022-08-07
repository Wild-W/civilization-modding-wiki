---
tags:
- EffectType
title: EFFECT_STEAL_POP_ON_PLOT_TO_CREATE_UNIT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_STEAL_POP_ON_PLOT_TO_CREATE_UNIT
>
> * Class: `Unknown`
> * Parameters:
>	* AllowAlternativeLocation `Unknown`
>	* AllowUniqueOverride `Unknown`
>	* Amount `Unknown`
>	* UnitType `Unknown`

## Samples

```SQL {title="TOWERDEFENSE_KILL_POP_AND_SPAWN_ZOMBIE_ON_DISTRICT_ATTACKS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"TOWERDEFENSE_KILL_POP_AND_SPAWN_ZOMBIE_ON_DISTRICT_ATTACKS",
		"MODIFIER_ALL_COMBAT_RESULTS_STEAL_POPULATION_AND_SPAWN_UNIT",
		"SHOULD_DISTRICT_ATTACK_SPAWN_ZOMBIE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TOWERDEFENSE_KILL_POP_AND_SPAWN_ZOMBIE_ON_DISTRICT_ATTACKS",
		"AllowAlternativeLocation",
		1
	),
	(
		"TOWERDEFENSE_KILL_POP_AND_SPAWN_ZOMBIE_ON_DISTRICT_ATTACKS",
		"AllowUniqueOverride",
		0
	),
	(
		"TOWERDEFENSE_KILL_POP_AND_SPAWN_ZOMBIE_ON_DISTRICT_ATTACKS",
		"Amount",
		1
	),
	(
		"TOWERDEFENSE_KILL_POP_AND_SPAWN_ZOMBIE_ON_DISTRICT_ATTACKS",
		"UnitType",
		"UNIT_MODE_ZOMBIE"
	);
	
```

