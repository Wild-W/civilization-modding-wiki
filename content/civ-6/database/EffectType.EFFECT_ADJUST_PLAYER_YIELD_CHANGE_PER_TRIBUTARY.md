---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_YIELD_CHANGE_PER_TRIBUTARY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_YIELD_CHANGE_PER_TRIBUTARY
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples
```SQL {title="RAJ_GOLDPERTRIBUTARY"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"RAJ_GOLDPERTRIBUTARY",
		"MODIFIER_PLAYER_ADJUST_YIELD_CHANGE_PER_TRIBUTARY"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"RAJ_GOLDPERTRIBUTARY",
		"Amount",
		2
	),
	(
		"RAJ_GOLDPERTRIBUTARY",
		"YieldType",
		"YIELD_GOLD"
	);
	
```

