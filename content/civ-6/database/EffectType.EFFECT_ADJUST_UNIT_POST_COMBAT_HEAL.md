---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_POST_COMBAT_HEAL
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_POST_COMBAT_HEAL
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="TOMYRIS_HEAL_AFTER_DEFEATING_UNIT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TOMYRIS_HEAL_AFTER_DEFEATING_UNIT",
		"MODIFIER_PLAYER_UNIT_ADJUST_HEAL_FROM_COMBAT"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TOMYRIS_HEAL_AFTER_DEFEATING_UNIT",
		"Amount",
		30
	);
	
```

