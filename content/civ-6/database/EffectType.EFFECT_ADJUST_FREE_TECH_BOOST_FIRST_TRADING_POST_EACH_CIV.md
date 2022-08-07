---
tags:
- EffectType
title: EFFECT_ADJUST_FREE_TECH_BOOST_FIRST_TRADING_POST_EACH_CIV
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_FREE_TECH_BOOST_FIRST_TRADING_POST_EACH_CIV
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Unknown`

## Samples

```SQL {title="TRAIT_TRADING_POST_TECH_BOOST"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_TRADING_POST_TECH_BOOST",
		"MODIFIER_PLAYER_ADJUST_FREE_TECH_BOOST_FIRST_TRADING_POST_EACH_CIV"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_TRADING_POST_TECH_BOOST",
		"Amount",
		1
	);
	
```

