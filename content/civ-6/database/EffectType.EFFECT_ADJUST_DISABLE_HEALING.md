---
tags:
- EffectType
title: EFFECT_ADJUST_DISABLE_HEALING
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_DISABLE_HEALING
>
> * Class: `PLAYERS`
> * Parameters:
>	* Disable `Boolean`
>	* Foreign `Boolean`

## Samples
```SQL {title="TWILIGHTVALOR_NO_FOREIGN_HEAL"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TWILIGHTVALOR_NO_FOREIGN_HEAL",
		"MODIFIER_PLAYER_DISABLE_HEALING"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TWILIGHTVALOR_NO_FOREIGN_HEAL",
		"Disable",
		1
	),
	(
		"TWILIGHTVALOR_NO_FOREIGN_HEAL",
		"Foreign",
		1
	);
	
```

