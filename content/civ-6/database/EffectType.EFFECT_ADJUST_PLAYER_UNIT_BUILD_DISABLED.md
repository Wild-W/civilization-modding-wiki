---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_UNIT_BUILD_DISABLED
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_UNIT_BUILD_DISABLED
>
> * Class: `PLAYERS`
> * Parameters:
>	* UnitType `String`
>		* [Units.UnitType]

## Samples

```SQL {title="ISOLATIONISM_DISABLE_BUILD_SETTLER"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"ISOLATIONISM_DISABLE_BUILD_SETTLER",
		"MODIFIER_PLAYER_UNIT_BUILD_DISABLED"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"ISOLATIONISM_DISABLE_BUILD_SETTLER",
		"UnitType",
		"UNIT_SETTLER"
	);
	
```

