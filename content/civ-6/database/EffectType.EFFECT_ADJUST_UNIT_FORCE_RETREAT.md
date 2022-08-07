---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_FORCE_RETREAT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_FORCE_RETREAT
>
> * Class: `UNITS`
> * Parameters:
>	* ForceRetreat `Boolean`

## Samples

```SQL {title="HUSSAR_FORCE_RETREAT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"HUSSAR_FORCE_RETREAT",
		"MODIFIER_UNIT_ADJUST_FORCE_RETREAT"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"HUSSAR_FORCE_RETREAT",
		"ForceRetreat",
		1
	);
	
```

