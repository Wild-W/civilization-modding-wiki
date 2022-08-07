---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_VALID_UNIT_BUILD
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_VALID_UNIT_BUILD
>
> * Class: `PLAYERS`
> * Parameters:
>	* UnitType `String`
>		* [Units.UnitType]

## Samples

```SQL {title="MINOR_CIV_LAHORE_NIHANG_UNIQUE_UNIT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"MINOR_CIV_LAHORE_NIHANG_UNIQUE_UNIT",
		"MODIFIER_PLAYER_ADJUST_VALID_UNIT_BUILD"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"MINOR_CIV_LAHORE_NIHANG_UNIQUE_UNIT",
		"UnitType",
		"UNIT_LAHORE_NIHANG"
	);
	
```

