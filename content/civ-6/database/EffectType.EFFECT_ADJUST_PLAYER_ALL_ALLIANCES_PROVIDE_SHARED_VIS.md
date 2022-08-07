---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_ALL_ALLIANCES_PROVIDE_SHARED_VIS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_ALL_ALLIANCES_PROVIDE_SHARED_VIS
>
> * Class: `PLAYERS`
> * Parameters:
>	* ShareVis `Boolean`

## Samples

```SQL {title="TRAIT_ALLIANCE_SHARED_VIS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_ALLIANCE_SHARED_VIS",
		"MODIFIER_PLAYER_ADJUST_ALLIANCES_SHARED_VIS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_ALLIANCE_SHARED_VIS",
		"ShareVis",
		1
	);
	
```

