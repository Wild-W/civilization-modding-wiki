---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_COMBAT_STRENGTH
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_COMBAT_STRENGTH
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Integer`
>		* [Units.UnitType]

## Samples
```SQL {title="NIHANG_BARRACKS_STRENGTH"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"NIHANG_BARRACKS_STRENGTH",
		"MODIFIER_UNIT_ADJUST_BASE_COMBAT_STRENGTH"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"NIHANG_BARRACKS_STRENGTH",
		"Amount",
		15
	);
	
```

