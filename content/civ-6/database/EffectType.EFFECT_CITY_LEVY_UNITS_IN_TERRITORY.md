---
tags:
- EffectType
title: EFFECT_CITY_LEVY_UNITS_IN_TERRITORY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_CITY_LEVY_UNITS_IN_TERRITORY
>
> * Class: `Unknown`
> * Parameters:
>	* Duration `Unknown`
>	* UnitType `Unknown`

## Samples

```SQL {title="PROJECT_COMPLETION_ZOMBIES_SHORT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"PROJECT_COMPLETION_ZOMBIES_SHORT",
		"MODIFIER_CITY_LEVY_UNITS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"PROJECT_COMPLETION_ZOMBIES_SHORT",
		"Duration",
		15
	),
	(
		"PROJECT_COMPLETION_ZOMBIES_SHORT",
		"UnitType",
		"UNIT_MODE_ZOMBIE"
	);
	
```

