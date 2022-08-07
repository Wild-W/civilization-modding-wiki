---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_NO_FOREIGN_SPREAD
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_NO_FOREIGN_SPREAD
>
> * Class: `UNITS`
> * Parameters:
>	* NoSpread `Boolean`

## Samples
```SQL {title="NO_FOREIGN_SPREAD"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"NO_FOREIGN_SPREAD",
		"MODIFIER_PLAYER_UNIT_ADJUST_NO_FOREIGN_SPREAD"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"NO_FOREIGN_SPREAD",
		"NoSpread",
		1
	);
	
```

