---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_PER_LUXURY_ATTACK_MODIFIER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_PER_LUXURY_ATTACK_MODIFIER
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="MONTEZUMA_COMBAT_BONUS_PER_LUXURY"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"MONTEZUMA_COMBAT_BONUS_PER_LUXURY",
		"MODIFIER_PLAYER_UNIT_ADJUST_PER_LUXURY_ATTACK_MODIFIER"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"MONTEZUMA_COMBAT_BONUS_PER_LUXURY",
		"Amount",
		1
	);
	
```

