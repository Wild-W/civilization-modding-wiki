---
tags:
- EffectType
title: EFFECT_GRANT_COMBAT_ADJACENCY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_GRANT_COMBAT_ADJACENCY
>
> * Class: `PLAYERS`
> * Parameters:
>	* Enable `Boolean`

## Samples

```SQL {title="CIVIC_GRANT_COMBAT_ADJACENCY_BONUS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"CIVIC_GRANT_COMBAT_ADJACENCY_BONUS",
		"MODIFIER_PLAYER_GRANT_COMBAT_ADJACENCY"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"CIVIC_GRANT_COMBAT_ADJACENCY_BONUS",
		"Enable",
		1
	);
	
```

