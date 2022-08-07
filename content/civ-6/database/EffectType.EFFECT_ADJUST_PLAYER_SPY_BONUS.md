---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_SPY_BONUS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_SPY_BONUS
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`
>	* Offense `Boolean`

## Samples

```SQL {title="CRYPTOGRAPHY_OFFENSE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"CRYPTOGRAPHY_OFFENSE",
		"MODIFIER_PLAYER_ADJUST_SPY_BONUS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"CRYPTOGRAPHY_OFFENSE",
		"Amount",
		1
	),
	(
		"CRYPTOGRAPHY_OFFENSE",
		"Offense",
		1
	);
	
```

