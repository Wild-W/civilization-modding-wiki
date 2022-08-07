---
tags:
- EffectType
title: EFFECT_GRANT_PLAYER_RANDOM_CIVIC
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_GRANT_PLAYER_RANDOM_CIVIC
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="BOLSHOI_THEATRE_FREE_CIVICS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent
	)
VALUES
	(
		"BOLSHOI_THEATRE_FREE_CIVICS",
		"MODIFIER_PLAYER_GRANT_RANDOM_CIVIC",
		1,
		1
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"BOLSHOI_THEATRE_FREE_CIVICS",
		"Amount",
		2
	);
	
```

