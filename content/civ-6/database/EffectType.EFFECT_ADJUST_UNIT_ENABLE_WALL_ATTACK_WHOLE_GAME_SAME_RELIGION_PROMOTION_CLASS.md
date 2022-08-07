---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_ENABLE_WALL_ATTACK_WHOLE_GAME_SAME_RELIGION_PROMOTION_CLASS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_ENABLE_WALL_ATTACK_WHOLE_GAME_SAME_RELIGION_PROMOTION_CLASS
>
> * Class: `Unknown`
> * Parameters:
>	* PromotionClass `Unknown`

## Samples

```SQL {title="TRAIT_ENABLE_WALL_ATTACK_LIGHT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_ENABLE_WALL_ATTACK_LIGHT",
		"MODIFIER_PLAYER_ADJUST_ENABLE_WALL_ATTACK_WHOLE_GAME_SAME_RELIGION_PROMOTION_CLASS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_ENABLE_WALL_ATTACK_LIGHT",
		"PromotionClass",
		"PROMOTION_CLASS_LIGHT_CAVALRY"
	);
	
```

