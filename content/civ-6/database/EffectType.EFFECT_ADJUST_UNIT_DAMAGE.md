---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_DAMAGE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_DAMAGE
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="TRAIT_TOWORLDSEND_HEAL_ON_WONDER_CAPTURE_MODIFIER"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent
	)
VALUES
	(
		"TRAIT_TOWORLDSEND_HEAL_ON_WONDER_CAPTURE_MODIFIER",
		"MODIFIER_PLAYER_UNITS_ADJUST_DAMAGE",
		1,
		1
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_TOWORLDSEND_HEAL_ON_WONDER_CAPTURE_MODIFIER",
		"Amount",
		"-100"
	);
	
```

