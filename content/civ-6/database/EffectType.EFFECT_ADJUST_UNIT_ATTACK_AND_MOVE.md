---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_ATTACK_AND_MOVE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_ATTACK_AND_MOVE
>
> * Class: `UNITS`
> * Parameters:
>	* CanMove `Boolean`

## Samples

```SQL {title="COSSACK_MOVE_AND_ATTACK"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"COSSACK_MOVE_AND_ATTACK",
		"MODIFIER_PLAYER_UNIT_ADJUST_ATTACK_AND_MOVE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"COSSACK_MOVE_AND_ATTACK",
		"CanMove",
		1
	);
	
```

