---
tags:
- EffectType
title: EFFECT_ADJUST_RESOURCE_POWER_PROVIDED_GOVERNOR
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_RESOURCE_POWER_PROVIDED_GOVERNOR
>
> * Class: `GOVERNORS`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="INDUSTRIALIST_RESOURCE_POWER_PROVIDED"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"INDUSTRIALIST_RESOURCE_POWER_PROVIDED",
		"MODIFIER_GOVERNOR_ADJUST_RESOURCE_POWER_PROVIDED_GOVERNOR"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"INDUSTRIALIST_RESOURCE_POWER_PROVIDED",
		"Amount",
		1
	);
	
```

