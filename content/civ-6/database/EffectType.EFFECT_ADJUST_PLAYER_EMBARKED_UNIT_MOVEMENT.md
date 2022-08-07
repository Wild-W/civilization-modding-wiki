---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_EMBARKED_UNIT_MOVEMENT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_EMBARKED_UNIT_MOVEMENT
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="GREATLIGHTHOUSE_ADJUST_EMBARKED_MOVEMENT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"GREATLIGHTHOUSE_ADJUST_EMBARKED_MOVEMENT",
		"MODIFIER_PLAYER_ADJUST_EMBARKED_MOVEMENT"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"GREATLIGHTHOUSE_ADJUST_EMBARKED_MOVEMENT",
		"Amount",
		1
	);
	
```

