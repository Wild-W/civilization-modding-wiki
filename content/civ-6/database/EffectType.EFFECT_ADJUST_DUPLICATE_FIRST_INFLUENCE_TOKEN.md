---
tags:
- EffectType
title: EFFECT_ADJUST_DUPLICATE_FIRST_INFLUENCE_TOKEN
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_DUPLICATE_FIRST_INFLUENCE_TOKEN
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="DIPLOMATICLEAGUE_DUPLICATEFIRSTINFLUENCETOKEN"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"DIPLOMATICLEAGUE_DUPLICATEFIRSTINFLUENCETOKEN",
		"MODIFIER_PLAYER_ADJUST_DUPLICATE_FIRST_INFLUENCE_TOKEN"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"DIPLOMATICLEAGUE_DUPLICATEFIRSTINFLUENCETOKEN",
		"Amount",
		1
	);
	
```

