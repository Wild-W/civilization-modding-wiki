---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_SEA_MOVEMENT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_SEA_MOVEMENT
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="MATHEMATICS_ADJUST_SEA_MOVEMENT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"MATHEMATICS_ADJUST_SEA_MOVEMENT",
		"MODIFIER_PLAYER_UNITS_ADJUST_SEA_MOVEMENT"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"MATHEMATICS_ADJUST_SEA_MOVEMENT",
		"Amount",
		1
	);
	
```

