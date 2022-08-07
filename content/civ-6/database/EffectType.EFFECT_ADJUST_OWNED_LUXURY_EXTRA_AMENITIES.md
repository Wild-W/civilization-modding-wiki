---
tags:
- EffectType
title: EFFECT_ADJUST_OWNED_LUXURY_EXTRA_AMENITIES
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_OWNED_LUXURY_EXTRA_AMENITIES
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="TRAIT_OWNED_LUXURY_EXTRA_AMENITIES"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_OWNED_LUXURY_EXTRA_AMENITIES",
		"MODIFIER_PLAYER_OWNED_LUXURY_EXTRA_AMENITIES"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_OWNED_LUXURY_EXTRA_AMENITIES",
		"Amount",
		2
	);
	
```

