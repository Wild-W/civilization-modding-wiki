---
tags:
- EffectType
title: EFFECT_GRANT_PLAYER_FAITH_FROM_HARVEST
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_GRANT_PLAYER_FAITH_FROM_HARVEST
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="GODDESS_OF_THE_HARVEST_HARVEST_MODIFIER"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"GODDESS_OF_THE_HARVEST_HARVEST_MODIFIER",
		"MODIFIER_PLAYER_GRANT_FAITH_FROM_HARVEST"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"GODDESS_OF_THE_HARVEST_HARVEST_MODIFIER",
		"Amount",
		100
	);
	
```
