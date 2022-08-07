---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_ENTER_FOREIGN_LANDS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_ENTER_FOREIGN_LANDS
>
> * Class: `UNITS`
> * Parameters:
>	* Enter `Boolean`

## Samples

```SQL {title="MOD_ENTER_FOREIGN_LANDS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"MOD_ENTER_FOREIGN_LANDS",
		"MODIFIER_PLAYER_UNIT_ADJUST_ENTER_FOREIGN_LANDS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"MOD_ENTER_FOREIGN_LANDS",
		"Enter",
		1
	);
	
```

