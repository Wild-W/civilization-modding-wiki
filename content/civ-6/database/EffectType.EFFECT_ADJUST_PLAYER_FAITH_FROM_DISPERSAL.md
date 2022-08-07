---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_FAITH_FROM_DISPERSAL
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_FAITH_FROM_DISPERSAL
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="INITIATION_RITES_FAITH_DISPERSAL_MODIFIER"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"INITIATION_RITES_FAITH_DISPERSAL_MODIFIER",
		"MODIFIER_PLAYER_ADJUST_FAITH_FROM_DISPERSAL"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"INITIATION_RITES_FAITH_DISPERSAL_MODIFIER",
		"Amount",
		50
	);
	
```

