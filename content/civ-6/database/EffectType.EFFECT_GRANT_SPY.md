---
tags:
- EffectType
title: EFFECT_GRANT_SPY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_GRANT_SPY
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="CIVIC_GRANT_SPY"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"CIVIC_GRANT_SPY",
		"MODIFIER_PLAYER_GRANT_SPY"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"CIVIC_GRANT_SPY",
		"Amount",
		1
	);
	
```

