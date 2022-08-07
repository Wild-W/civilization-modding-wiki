---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_CITY_TILES
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_CITY_TILES
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="TRAIT_INCREASED_TILES"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_INCREASED_TILES",
		"MODIFIER_PLAYER_ADJUST_CITY_TILES"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_INCREASED_TILES",
		"Amount",
		5
	);
	
```

