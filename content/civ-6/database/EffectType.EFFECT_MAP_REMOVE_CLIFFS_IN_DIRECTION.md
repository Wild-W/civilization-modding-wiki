---
tags:
- EffectType
title: EFFECT_MAP_REMOVE_CLIFFS_IN_DIRECTION
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_MAP_REMOVE_CLIFFS_IN_DIRECTION
>
> * Class: `Unknown`
> * Parameters:
>	* Radius `Integer`

## Samples
```SQL {title="GOLDENGATE_REMOVE_CLIFFS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"GOLDENGATE_REMOVE_CLIFFS",
		"MODIFIER_MAP_REMOVE_CLIFFS_IN_DIRECTION"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"GOLDENGATE_REMOVE_CLIFFS",
		"Radius",
		1
	);
	
```

