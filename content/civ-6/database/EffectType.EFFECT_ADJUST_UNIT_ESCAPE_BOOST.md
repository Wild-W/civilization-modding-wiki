---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_ESCAPE_BOOST
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_ESCAPE_BOOST
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="SPY_ACE_DRIVER"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"SPY_ACE_DRIVER",
		"MODIFIER_PLAYER_UNIT_ESCAPE_BOOST"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"SPY_ACE_DRIVER",
		"Amount",
		4
	);
	
```

