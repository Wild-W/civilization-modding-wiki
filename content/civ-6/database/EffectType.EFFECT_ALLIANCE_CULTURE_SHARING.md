---
tags:
- EffectType
title: EFFECT_ALLIANCE_CULTURE_SHARING
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ALLIANCE_CULTURE_SHARING
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="ALLIANCE_CULTURE_SHARING_FROM_ALLY"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"ALLIANCE_CULTURE_SHARING_FROM_ALLY",
		"MODIFIER_ALLIANCE_PLAYERS_CULTURE_FROM_ALLY"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"ALLIANCE_CULTURE_SHARING_FROM_ALLY",
		"Amount",
		10
	);
	
```

