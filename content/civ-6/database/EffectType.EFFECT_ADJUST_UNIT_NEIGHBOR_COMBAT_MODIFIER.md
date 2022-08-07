---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_NEIGHBOR_COMBAT_MODIFIER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_NEIGHBOR_COMBAT_MODIFIER
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="AMBIORIX_NEIGHBOR_COMBAT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"AMBIORIX_NEIGHBOR_COMBAT",
		"MODIFIER_PLAYER_UNIT_ADJUST_COMBAT_FOR_NUMBER_NEIGHBORS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"AMBIORIX_NEIGHBOR_COMBAT",
		"Amount",
		2
	);
	
```

