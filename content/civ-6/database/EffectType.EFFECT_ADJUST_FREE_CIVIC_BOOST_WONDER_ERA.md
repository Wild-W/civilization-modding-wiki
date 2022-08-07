---
tags:
- EffectType
title: EFFECT_ADJUST_FREE_CIVIC_BOOST_WONDER_ERA
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_FREE_CIVIC_BOOST_WONDER_ERA
>
> * Class: `Unknown`
> * Parameters:
>	* Amount `Unknown`

## Samples

```SQL {title="TRAIT_CIVIC_BOOST_WONDER_ERA"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_CIVIC_BOOST_WONDER_ERA",
		"MODIFIER_PLAYER_ADJUST_FREE_CIVIC_BOOST_WONDER_ERA"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_CIVIC_BOOST_WONDER_ERA",
		"Amount",
		1
	);
	
```

