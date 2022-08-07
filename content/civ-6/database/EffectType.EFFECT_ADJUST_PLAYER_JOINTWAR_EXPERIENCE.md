---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_JOINTWAR_EXPERIENCE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_JOINTWAR_EXPERIENCE
>
> * Class: `PLAYERS`
> * Parameters:
>	* Range `Integer`

## Samples

```SQL {title="TRAIT_ADJUST_JOINTWAR_EXPERIENCE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_ADJUST_JOINTWAR_EXPERIENCE",
		"MODIFIER_PLAYER_ADJUST_JOINTWAR_EXPERIENCE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_ADJUST_JOINTWAR_EXPERIENCE",
		"Range",
		5
	);
	
```

