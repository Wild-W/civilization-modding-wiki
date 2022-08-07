---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_JOINTWAR_PLUNDER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_JOINTWAR_PLUNDER
>
> * Class: `PLAYERS`
> * Parameters:
>	* Multiplier `Integer`

## Samples
```SQL {title="TRAIT_ADJUST_JOINTWAR_PLUNDER"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_ADJUST_JOINTWAR_PLUNDER",
		"MODIFIER_PLAYER_ADJUST_JOINTWAR_PLUNDER"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_ADJUST_JOINTWAR_PLUNDER",
		"Multiplier",
		100
	);
	
```

