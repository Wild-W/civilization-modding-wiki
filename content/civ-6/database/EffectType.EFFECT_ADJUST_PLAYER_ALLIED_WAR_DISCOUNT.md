---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_ALLIED_WAR_DISCOUNT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_ALLIED_WAR_DISCOUNT
>
> * Class: `PLAYERS`
> * Parameters:
>	* Discount `Integer`

## Samples

```SQL {title="TRAIT_ADJUST_ALLIED_WAR_DISCOUNT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_ADJUST_ALLIED_WAR_DISCOUNT",
		"MODIFIER_PLAYER_ADJUST_ALLIED_WAR_DISCOUNT"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_ADJUST_ALLIED_WAR_DISCOUNT",
		"Discount",
		150
	);
	
```

