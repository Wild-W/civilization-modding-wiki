---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_ENABLE_WALL_ATTACK_WHOLE_GAME_PROMOTION_CLASS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_ENABLE_WALL_ATTACK_WHOLE_GAME_PROMOTION_CLASS
>
> * Class: `UNITS`
> * Parameters:
>	* PromotionClass `String`

## Samples

```SQL {title="MINOR_CIV_AKKAD_ENABLE_WALL_ATTACK_WHOLE_GAME_MELEE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"MINOR_CIV_AKKAD_ENABLE_WALL_ATTACK_WHOLE_GAME_MELEE",
		"MODIFIER_PLAYER_UNITS_ADJUST_ENABLE_WALL_ATTACK_WHOLE_GAME_PROMOTION_CLASS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"MINOR_CIV_AKKAD_ENABLE_WALL_ATTACK_WHOLE_GAME_MELEE",
		"PromotionClass",
		"PROMOTION_CLASS_MELEE"
	);
	
```

