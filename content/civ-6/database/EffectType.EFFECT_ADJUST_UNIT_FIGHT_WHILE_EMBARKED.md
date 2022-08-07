---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_FIGHT_WHILE_EMBARKED
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_FIGHT_WHILE_EMBARKED
>
> * Class: `UNITS`
> * Parameters:
>	* CanFight `Boolean`

## Samples
```SQL {title="GDR_FIGHT_WHILE_EMBARKED"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"GDR_FIGHT_WHILE_EMBARKED",
		"MODIFIER_SINGLE_UNIT_ADJUST_FIGHT_WHILE_EMBARKED"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"GDR_FIGHT_WHILE_EMBARKED",
		"CanFight",
		1
	);
	
```

