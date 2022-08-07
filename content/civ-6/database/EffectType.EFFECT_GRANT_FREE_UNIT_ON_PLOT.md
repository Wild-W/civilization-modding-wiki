---
tags:
- EffectType
title: EFFECT_GRANT_FREE_UNIT_ON_PLOT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_GRANT_FREE_UNIT_ON_PLOT
>
> * Class: `Unknown`
> * Parameters:
>	* AllowAlternativeLocation `Unknown`
>	* AllowUniqueOverride `Unknown`
>	* UnitType `Unknown`

## Samples

```SQL {title="TOWERDEFENSE_SPAWN_ZOMBIE_ON_EACH_DEATH"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"TOWERDEFENSE_SPAWN_ZOMBIE_ON_EACH_DEATH",
		"MODIFIER_ALL_UNIT_DEATHS_SPAWN_UNIT",
		"SHOULD_SPAWN_ZOMBIE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TOWERDEFENSE_SPAWN_ZOMBIE_ON_EACH_DEATH",
		"AllowAlternativeLocation",
		1
	),
	(
		"TOWERDEFENSE_SPAWN_ZOMBIE_ON_EACH_DEATH",
		"AllowUniqueOverride",
		0
	),
	(
		"TOWERDEFENSE_SPAWN_ZOMBIE_ON_EACH_DEATH",
		"UnitType",
		"UNIT_MODE_ZOMBIE"
	);
	
```

