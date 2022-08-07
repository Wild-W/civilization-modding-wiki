---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_BOOST_ALL_SPIES
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_BOOST_ALL_SPIES
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Integer`
>	* Defense `Boolean`

## Samples
```SQL {title="SPY_QUARTERMASTER"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"SPY_QUARTERMASTER",
		"MODIFIER_PLAYER_UNIT_BOOST_ALL_SPIES"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"SPY_QUARTERMASTER",
		"Amount",
		1
	);
	
```

```SQL {title="SPY_POLYGRAPH"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"SPY_POLYGRAPH",
		"MODIFIER_PLAYER_UNIT_BOOST_ALL_SPIES"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"SPY_POLYGRAPH",
		"Amount",
		1
	),
	(
		"SPY_POLYGRAPH",
		"Defense",
		1
	);
	
```

