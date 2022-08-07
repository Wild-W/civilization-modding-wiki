---
tags:
- EffectType
title: EFFECT_ADJUST_TECHNOLOGY_BOOST
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_TECHNOLOGY_BOOST
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="TRAIT_TECHNOLOGY_BOOST"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_TECHNOLOGY_BOOST",
		"MODIFIER_PLAYER_ADJUST_TECHNOLOGY_BOOST"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value,
		Extra
	)
VALUES
	(
		"TRAIT_TECHNOLOGY_BOOST",
		"Amount",
		10,
		"-1"
	);
	
```

