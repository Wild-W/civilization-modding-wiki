---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_SUPPORT_BONUS_MODIFIER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_SUPPORT_BONUS_MODIFIER
>
> * Class: `UNITS`
> * Parameters:
>	* Percent `Integer`

## Samples
```SQL {title="SQUARE_BONUS_SUPPORT_BONUS_MODIFIER"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"SQUARE_BONUS_SUPPORT_BONUS_MODIFIER",
		"MODIFIER_PLAYER_UNIT_ADJUST_SUPPORT_BONUS_MODIFIER"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"SQUARE_BONUS_SUPPORT_BONUS_MODIFIER",
		"Percent",
		100
	);
	
```

