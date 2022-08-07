---
tags:
- EffectType
title: EFFECT_BECOME_CITY_SUZERAIN
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_BECOME_CITY_SUZERAIN
>
> * Class: `Unknown`
> * Parameters:
>	* RemoveOthers `Unknown`

## Samples
```SQL {title="GREATPERSON_CITY_STATE_STEAL_ENVOYS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent
	)
VALUES
	(
		"GREATPERSON_CITY_STATE_STEAL_ENVOYS",
		"MODIFIER_UNIT_BECOME_CITY_SUZERAIN",
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
		"GREATPERSON_CITY_STATE_STEAL_ENVOYS",
		"RemoveOthers",
		1
	);
	
```

