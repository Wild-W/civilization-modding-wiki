---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_TOURISM
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_TOURISM
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="COMPUTERS_BOOST_ALL_TOURISM"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"COMPUTERS_BOOST_ALL_TOURISM",
		"MODIFIER_PLAYER_ADJUST_TOURISM"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"COMPUTERS_BOOST_ALL_TOURISM",
		"Amount",
		25
	);
	
```

