---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_ENABLE_WALL_ATTACK_PROMOTION_CLASS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_ENABLE_WALL_ATTACK_PROMOTION_CLASS
>
> * Class: `UNITS`
> * Parameters:
>	* PromotionClass `String`

## Samples

```SQL {title="ENABLE_WALL_ATTACK_MELEE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"ENABLE_WALL_ATTACK_MELEE",
		"MODIFIER_PLAYER_UNIT_ADJUST_ENABLE_WALL_ATTACK_PROMOTION_CLASS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"ENABLE_WALL_ATTACK_MELEE",
		"PromotionClass",
		"PROMOTION_CLASS_MELEE"
	);
	
```

