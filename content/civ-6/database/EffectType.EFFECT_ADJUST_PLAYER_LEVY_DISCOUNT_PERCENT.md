---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_LEVY_DISCOUNT_PERCENT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_LEVY_DISCOUNT_PERCENT
>
> * Class: `PLAYERS`
> * Parameters:
>	* Percent `Integer`

## Samples

```SQL {title="TRAIT_LEVY_DISCOUNT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_LEVY_DISCOUNT",
		"MODIFIER_PLAYER_ADJUST_LEVY_DISCOUNT_PERCENT"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_LEVY_DISCOUNT",
		"Percent",
		50
	);
	
```

