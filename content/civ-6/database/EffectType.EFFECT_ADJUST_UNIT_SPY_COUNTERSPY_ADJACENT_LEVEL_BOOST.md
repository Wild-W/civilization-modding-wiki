---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_SPY_COUNTERSPY_ADJACENT_LEVEL_BOOST
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_SPY_COUNTERSPY_ADJACENT_LEVEL_BOOST
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="SPY_SURVEILLANCE_ADJACENT_LEVEL"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"SPY_SURVEILLANCE_ADJACENT_LEVEL",
		"MODIFIER_SINGLE_UNIT_ADJUST_SPY_COUNTERSPY_ADJACENT_LEVEL_BOOST"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"SPY_SURVEILLANCE_ADJACENT_LEVEL",
		"Amount",
		1
	);
	
```

