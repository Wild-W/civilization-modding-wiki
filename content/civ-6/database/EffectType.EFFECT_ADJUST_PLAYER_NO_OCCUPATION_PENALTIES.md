---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_NO_OCCUPATION_PENALTIES
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_NO_OCCUPATION_PENALTIES
>
> * Class: `CITIES`
> * Parameters:
>	* NoPenalties `Boolean`

## Samples
```SQL {title="TRAIT_FALLBABYLON_NO_OCCUPATION_PENALTIES"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_FALLBABYLON_NO_OCCUPATION_PENALTIES",
		"MODIFIER_PLAYER_ADJUST_NO_OCCUPATION_PENALTIES"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_FALLBABYLON_NO_OCCUPATION_PENALTIES",
		"NoPenalties",
		1
	);
	
```

