---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_MAX_WARMONGER_PERCENT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_MAX_WARMONGER_PERCENT
>
> * Class: `PLAYERS`
> * Parameters:
>	* MaxPercent `Integer`

## Samples
```SQL {title="TRAIT_FALLBABYLON_WARMONGER_MAX"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_FALLBABYLON_WARMONGER_MAX",
		"MODIFIER_PLAYER_ADJUST_MAX_WARMONGER_PERCENT"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_FALLBABYLON_WARMONGER_MAX",
		"MaxPercent",
		100
	);
	
```

