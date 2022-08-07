---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_GRIEVANCE_DECAY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_GRIEVANCE_DECAY
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="TRAIT_SHORT_LIFE_GRIEVANCE_DECAY"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_SHORT_LIFE_GRIEVANCE_DECAY",
		"MODIFIER_PLAYER_ADJUST_GRIEVANCE_DECAY"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_SHORT_LIFE_GRIEVANCE_DECAY",
		"Amount",
		100
	);
	
```

