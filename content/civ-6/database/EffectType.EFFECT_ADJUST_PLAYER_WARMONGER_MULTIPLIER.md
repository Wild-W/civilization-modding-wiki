---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_WARMONGER_MULTIPLIER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_WARMONGER_MULTIPLIER
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="NONAGENDA_IGNORE_WARMONGERING"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"NONAGENDA_IGNORE_WARMONGERING",
		"MODIFIER_PLAYER_ADJUST_WARMONGER_MULTIPLIER"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"NONAGENDA_IGNORE_WARMONGERING",
		"Amount",
		0
	);
	
```

