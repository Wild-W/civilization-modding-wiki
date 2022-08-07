---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_TOURISM_FAVOR
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_TOURISM_FAVOR
>
> * Class: `PLAYERS`
> * Parameters:
>	* Favor `Integer`
>	* Tourism `Integer`

## Samples
```SQL {title="TRAIT_TOURISM_INTO_FAVOR"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_TOURISM_INTO_FAVOR",
		"MODIFIER_PLAYER_ADJUST_TOURISM_INTO_FAVOR"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_TOURISM_INTO_FAVOR",
		"Favor",
		1
	),
	(
		"TRAIT_TOURISM_INTO_FAVOR",
		"Tourism",
		100
	);
	
```

