---
tags:
- EffectType
title: EFFECT_ADJUST_NUMBER_ALLIES_UNIT_COMBAT_BONUS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_NUMBER_ALLIES_UNIT_COMBAT_BONUS
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="HUSZAR_ALLIES_COMBAT_BONUS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"HUSZAR_ALLIES_COMBAT_BONUS",
		"MODIFIER_SINGLE_UNIT_ADJUST_COMBAT_FOR_NUMBER_ALLIES"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"HUSZAR_ALLIES_COMBAT_BONUS",
		"Amount",
		3
	);
	
```

