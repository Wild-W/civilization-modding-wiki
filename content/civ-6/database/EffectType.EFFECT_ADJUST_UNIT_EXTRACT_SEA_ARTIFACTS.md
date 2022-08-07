---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_EXTRACT_SEA_ARTIFACTS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_EXTRACT_SEA_ARTIFACTS
>
> * Class: `UNITS`
> * Parameters:
>	* Extract `Boolean`

## Samples

```SQL {title="CIVIC_EXTRACT_SEA_ARTIFACTS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"CIVIC_EXTRACT_SEA_ARTIFACTS",
		"MODIFIER_PLAYER_UNIT_ADJUST_EXTRACT_SEA_ARTIFACTS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"CIVIC_EXTRACT_SEA_ARTIFACTS",
		"Extract",
		1
	);
	
```

