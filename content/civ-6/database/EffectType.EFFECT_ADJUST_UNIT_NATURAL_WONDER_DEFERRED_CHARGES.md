---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_NATURAL_WONDER_DEFERRED_CHARGES
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_NATURAL_WONDER_DEFERRED_CHARGES
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="APOSTLE_NW_DEFERRED_CHARGES"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"APOSTLE_NW_DEFERRED_CHARGES",
		"MODIFIER_PLAYER_UNIT_ADJUST_NATURAL_WONDER_DEFERRED_CHARGES"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"APOSTLE_NW_DEFERRED_CHARGES",
		"Amount",
		3
	);
	
```

