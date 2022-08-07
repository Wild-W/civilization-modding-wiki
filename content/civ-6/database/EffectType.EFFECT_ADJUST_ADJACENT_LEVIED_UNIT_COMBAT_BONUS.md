---
tags:
- EffectType
title: EFFECT_ADJUST_ADJACENT_LEVIED_UNIT_COMBAT_BONUS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_ADJACENT_LEVIED_UNIT_COMBAT_BONUS
>
> * Class: `Unknown`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="BLACK_ARMY_ADJACENT_LEVY"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"BLACK_ARMY_ADJACENT_LEVY",
		"MODIFIER_SINGLE_UNIT_ADJUST_COMBAT_FOR_ADJACENT_LEVIED_UNITS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"BLACK_ARMY_ADJACENT_LEVY",
		"Amount",
		3
	);
	
```

