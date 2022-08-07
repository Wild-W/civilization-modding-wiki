---
tags:
- EffectType
title: EFFECT_GRANT_PLAYER_FAITH_FROM_REMOVE_FEATURE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_GRANT_PLAYER_FAITH_FROM_REMOVE_FEATURE
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="GODDESS_OF_THE_HARVEST_REMOVE_FEATURE_MODIFIER"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"GODDESS_OF_THE_HARVEST_REMOVE_FEATURE_MODIFIER",
		"MODIFIER_PLAYER_GRANT_FAITH_FROM_REMOVE_FEATURE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"GODDESS_OF_THE_HARVEST_REMOVE_FEATURE_MODIFIER",
		"Amount",
		100
	);
	
```

