---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_BYPASS_COMBAT_UNIT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_BYPASS_COMBAT_UNIT
>
> * Class: `UNITS`
> * Parameters:
>	* Bypass `Boolean`

## Samples

```SQL {title="ATTACK_BYPASS_COMBAT_UNIT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"ATTACK_BYPASS_COMBAT_UNIT",
		"MODIFIER_PLAYER_UNIT_ADJUST_BYPASS_COMBAT_UNIT"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"ATTACK_BYPASS_COMBAT_UNIT",
		"Bypass",
		1
	);
	
```

