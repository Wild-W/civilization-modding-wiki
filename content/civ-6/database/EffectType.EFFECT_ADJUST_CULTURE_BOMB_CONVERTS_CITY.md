---
tags:
- EffectType
title: EFFECT_ADJUST_CULTURE_BOMB_CONVERTS_CITY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CULTURE_BOMB_CONVERTS_CITY
>
> * Class: `PLAYERS`
> * Parameters:
>	* ConvertsCity `Boolean`

## Samples

```SQL {title="TRAIT_CULTURE_BOMB_CONVERTS_CITY"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_CULTURE_BOMB_CONVERTS_CITY",
		"MODIFIER_PLAYER_ADJUST_CULTURE_BOMB_CONVERTS_CITY"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_CULTURE_BOMB_CONVERTS_CITY",
		"ConvertsCity",
		1
	);
	
```

