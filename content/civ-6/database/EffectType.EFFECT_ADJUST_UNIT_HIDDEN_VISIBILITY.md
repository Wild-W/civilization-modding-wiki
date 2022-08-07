---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_HIDDEN_VISIBILITY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_HIDDEN_VISIBILITY
>
> * Class: `UNITS`
> * Parameters:
>	* Hidden `Boolean`

## Samples

```SQL {title="UNIT_HIDDEN_VISIBILITY"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"UNIT_HIDDEN_VISIBILITY",
		"MODIFIER_PLAYER_UNIT_ADJUST_HIDDEN_VISIBILITY"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"UNIT_HIDDEN_VISIBILITY",
		"Hidden",
		1
	);
	
```

